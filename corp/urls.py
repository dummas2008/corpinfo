from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.company_list, name='company_list'),
]