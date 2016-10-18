#coding=utf-8
from django.db import models
from datetime import datetime


OS_TYPE_CHOICES = (('windows','Windows Server'),('linux','Linux 64'),)
APPLICATION_STATUS_CHOICES = (('draft','草稿中'),('submitted','已提交'),)

# Create your models here.
class ReleaseApplication(models.Model):
    id = models.AutoField(primary_key=True)
    appname = models.CharField(max_length=200,verbose_name=u"应用名称",help_text=u"要发布的应用名称")
    version = models.CharField(max_length=200,blank=True,verbose_name=u"应用版本",help_text=u"要发布的应用版本")
    team_name = models.CharField(max_length=200,verbose_name=u"团队名称",help_text=u"负责应用的团队名称")
    responsible_username = models.CharField(max_length=200,verbose_name=u"负责人名称",blank=True,help_text=u"应用的负责人")
    application_username = models.CharField(max_length=200,verbose_name=u"申请人名称",help_text=u"申请人的名称")
    application_note = models.CharField(max_length=200,verbose_name=u"应用描述",blank=True,help_text=u"关于应用的描述")
    deploy_note = models.TextField(verbose_name=u"发布说明",help_text=u"此次发布的步骤说明")

    os_type = models.CharField(max_length=100, choices=OS_TYPE_CHOICES, default='linux', verbose_name=u'操作系统', help_text=u'应用部署的操作系统')
    instance_count = models.IntegerField(default=2,verbose_name=u"应用部署的实例数",help_text=u"申请应用部署的实例数量")
    status = models.CharField(max_length=100, choices=APPLICATION_STATUS_CHOICES,default='draft', verbose_name=u'申请单状态', help_text=u'申请单状态')
    
    created_date = models.DateTimeField(default=datetime.now, blank=True,verbose_name=u'创建时间')
    updated_date = models.DateTimeField(default=datetime.now, blank=True,verbose_name=u'更新时间')
    remark = models.CharField(max_length=200,blank=True,verbose_name=u"备注",help_text=u"备注")