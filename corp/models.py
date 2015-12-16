from django.db import models

# Create your models here.
class Company(models.Model):
    Code = models.CharField(max_length=200, null=True, blank=True)
    CompanyName = models.CharField(max_length=200)
    CompanyProfile = models.TextField(null=True, blank=True)
    CompanyURL = models.CharField(max_length=200, null=True, blank=True)
    LastUpdate = models.CharField(max_length=200, null=True, blank=True)
    Contact = models.CharField(max_length=200, null=True, blank=True)
    Telephone = models.CharField(max_length=200, null=True, blank=True)
    MobilePhnoe = models.CharField(max_length=200, null=True, blank=True)
    WangWangId = models.CharField(max_length=200, null=True, blank=True)
    Fax = models.CharField(max_length=200, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
    MainProductService = models.CharField(max_length=200, null=True, blank=True)
    MainIndustry = models.CharField(max_length=200, null=True, blank=True)
    BusinessMode = models.CharField(max_length=200, null=True, blank=True)
    ServiceType = models.CharField(max_length=200, null=True, blank=True)
    OEMOrCustomService = models.CharField(max_length=200, null=True, blank=True)
    RegisterCapital = models.CharField(max_length=200, null=True, blank=True)
    FoundTime = models.CharField(max_length=200, null=True, blank=True)
    RegisterPlace = models.CharField(max_length=200, null=True, blank=True)
    CompanyType = models.CharField(max_length=200, null=True, blank=True)
    LegalRepresentative = models.CharField(max_length=200, null=True, blank=True)
    RegisterNo = models.CharField(max_length=200, null=True, blank=True)
    ProcessMethod = models.CharField(max_length=200, null=True, blank=True)
    IndustrialArt = models.CharField(max_length=200, null=True, blank=True)
    ManageCertification = models.CharField(max_length=200, null=True, blank=True)
    QualityCertification = models.CharField(max_length=200, null=True, blank=True)
    Warehouse = models.CharField(max_length=200, null=True, blank=True)
    EmpolyeeCount = models.CharField(max_length=200, null=True, blank=True)
    DeveloperCount = models.CharField(max_length=200, null=True, blank=True)
    PlantArea = models.CharField(max_length=200, null=True, blank=True)
    MainSalesRegion = models.CharField(max_length=200, null=True, blank=True)
    MainCustomerGroup = models.CharField(max_length=200, null=True, blank=True)
    ServiceField = models.CharField(max_length=200, null=True, blank=True)
    AgentLevel = models.CharField(max_length=200, null=True, blank=True)
    BrandName = models.CharField(max_length=200, null=True, blank=True)
    MonthlyProduction = models.CharField(max_length=200, null=True, blank=True)
    AnnualTurnover = models.CharField(max_length=200, null=True, blank=True)
    AnnualExport = models.CharField(max_length=200, null=True, blank=True)
    QualityControl = models.CharField(max_length=200, null=True, blank=True)
    BankOfDeposit = models.CharField(max_length=200, null=True, blank=True)
    Account = models.CharField(max_length=200, null=True, blank=True)
    HomePage = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.CompanyName

#   "Code" : "",/*企业名称*/
#   "CompanyName" : "",/**/
#   "CompanyProfile" : "",/*主营产品*/
#   "CompanyURL" : "",/**/
#   "LastUpdate" : "",/**/
#   "Contact" : "",/*联系人*/
#   "Telephone" : "",/*联系电话*/
#   "MobilePhnoe" : "",/*手机号*/
#   "WangWangId" : "",/**/
#   "Fax" : "",/*传真*/
#   "Address" : "",/*地址*/
#   "PostCode" : "",/*邮编*/
#   "MainProductService" : "",/*主营产品或服务*/
#   "MainIndustry" : "",/*主营行业*/
#   "BusinessMode" : "",/*经营模式*/
#   "ServiceType" : "",/**/
#   "OEMOrCustomService" : "",/*是否提供加工/定制服务*/
#   "RegisterCapital" : "",/*注册资本*/
#   "FoundTime" : "",/*成立日期*/
#   "RegisterPlace" : "",/*企业注册地点*/
#   "CompanyType" : "",/*企业类型*/
#   "LegalRepresentative" : "",/*法定代表人*/
#   "RegisterNo" : "",/*注册号*/
#   "ProcessMethod" : "",/*加工方式*/
#   "IndustrialArt" : "",/*工艺类型*/
#   "ManageCertification" : "",/*资质证书*/
#   "QualityCertification" : "",/*质量证书*/
#   "Warehouse" : "",/*仓库*/
#   "EmpolyeeCount" : "",/*员工人数*/
#   "DeveloperCount" : "",/*研发人员人数*/
#   "PlantArea" : "",/*厂房面积 */
#   "MainSalesRegion" : "",/*主要销售区域*/
#   "MainCustomerGroup" : "",/*主要客户群体*/
#   "ServiceField" : "",/*服务领域*/
#   "AgentLevel" : "",/*代理级别*/
#   "BrandName" : "",/*品牌名称*/
#   "MonthlyProduction" : "",/*月产量*/
#   "AnnualTurnover" : "",/*年营业额*/
#   "AnnualExport" : "",/*年出口额 */
#   "QualityControl" : "",/*质量控制*/
#   "BankOfDeposit" : "",/*开户银行*/
#   "Account" : "",/*账号*/
#   "HomePage" : ""/*主页*/