from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.results import Error, Result, RowResult
from django.utils import six
import urllib
from .common import *
# Set default logging handler to avoid "No handler found" warnings.
# import logging
# try:  # Python 2.7+
#     from logging import NullHandler
# except ImportError:
#     class NullHandler(logging.Handler):
#         def emit(self, record):
#             pass
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
import json

try:
    from django.db.transaction import atomic, savepoint, savepoint_rollback, savepoint_commit  # noqa
except ImportError:
    from .django_compat import atomic, savepoint, savepoint_rollback, savepoint_commit  # noqa
 
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text 
    
from copy import deepcopy
import sys
import traceback 
from django.db.transaction import TransactionManagementError   
from .models import Company
# Register your models here.
#admin.site.register(Company)

class CompanyResource(resources.ModelResource):

    class Meta:
        model = Company
    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, **kwargs):
        result = Result()
        result.diff_headers = self.get_diff_headers()

        if use_transactions is None:
            use_transactions = self.get_use_transactions()

        if use_transactions is True:
            # when transactions are used we want to create/update/delete object
            # as transaction will be rolled back if dry_run is set
            real_dry_run = False
            sp1 = savepoint()
        else:
            real_dry_run = dry_run
        #logging.error(dataset)
        try:
            self.before_import(dataset, real_dry_run, **kwargs)
        except Exception as e:
            logging.exception(e)
            tb_info = traceback.format_exc(2)
            result.base_errors.append(Error(repr(e), tb_info))
            if raise_errors:
                if use_transactions:
                    savepoint_rollback(sp1)
                raise

        instance_loader = self._meta.instance_loader_class(self, dataset)
        url = 'http://api.dataduoduo.com/cgi/token?appid=15121101059459&secret=772D05E0-23D1-48F1-9969-7F1E49C5929D'
        r = get_content(url, decoded=False)
        info=json.loads(str(r,"utf-8"))
        logging.error(info)
        if info['code'] == 0:
            access_token = info['result']['token']
        for row in dataset.dict:
            try:
                row_result = RowResult()
                #logging.error(row['CompanyName'])                
                #logging.error(access_token)
                url = 'http://api.dataduoduo.com/companyinfo/companyinformation?companyname={}&accesstoken={}'.format(urllib.parse.quote(row['CompanyName']), access_token)
                
                #logging.error(url)
                r = get_content(url, decoded=False)
                #logging.error(r)
                info=json.loads(str(r,"utf-8"))
                if info['code'] == 0:
                    corp_info = info['result']
                    id = row['id']
                    row = corp_info[0]
                    row['id']=id
                    #logging.error(row)
                else:
                    logging.error("{} no found".format(row['CompanyName']))    
                instance, new = self.get_or_init_instance(instance_loader, row)
                if new:
                    row_result.import_type = RowResult.IMPORT_TYPE_NEW
                else:
                    row_result.import_type = RowResult.IMPORT_TYPE_UPDATE
                row_result.new_record = new
                original = deepcopy(instance)
                if self.for_delete(row, instance):
                    if new:
                        row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                        row_result.diff = self.get_diff(None, None,
                                                        real_dry_run)
                    else:
                        row_result.import_type = RowResult.IMPORT_TYPE_DELETE
                        self.delete_instance(instance, real_dry_run)
                        row_result.diff = self.get_diff(original, None,
                                                        real_dry_run)
                else:
                    self.import_obj(instance, row, real_dry_run)
                    if self.skip_row(instance, original):
                        row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                    else:
                        self.save_instance(instance, real_dry_run)
                        self.save_m2m(instance, row, real_dry_run)
                        # Add object info to RowResult for LogEntry
                        row_result.object_repr = force_text(instance)
                        row_result.object_id = instance.pk
                    row_result.diff = self.get_diff(original, instance,
                                                    real_dry_run)
            except Exception as e:
                # There is no point logging a transaction error for each row
                # when only the original error is likely to be relevant
                if not isinstance(e, TransactionManagementError):
                    logging.exception(e)
                tb_info = traceback.format_exc(2)
                row_result.errors.append(Error(e, tb_info, row))
                if raise_errors:
                    if use_transactions:
                        savepoint_rollback(sp1)
                    six.reraise(*sys.exc_info())
            if (row_result.import_type != RowResult.IMPORT_TYPE_SKIP or
                    self._meta.report_skipped):
                result.rows.append(row_result)

        if use_transactions:
            if dry_run or result.has_errors():
                savepoint_rollback(sp1)
            else:
                savepoint_commit(sp1)

        return result
        
        
class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource
    pass   

admin.site.register(Company, CompanyAdmin)     