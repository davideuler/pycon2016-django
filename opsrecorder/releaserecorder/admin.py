#coding:utf-8
from django.contrib import admin
from releaserecorder.models import ReleaseApplication
from django.contrib.admin import actions
from django.utils.html import format_html

def submit_application(modeladmin, request, queryset):
    queryset.update(status='submitted')

submit_application.short_description = "提交申请"


class ReleaseApplicationAdmin(admin.ModelAdmin):
    actions = [submit_application]
    
    def get_app_url(self,obj): #显示app的版本持续集成状态页面的链接
        return format_html(u'<a href="http://app.aliyun.com/%s/%s">状态</a>' % (obj.appname, obj.version)) 
    get_app_url.short_description = '持续集成状态'
    
    readonly_fields = ('created_date','updated_date','status',)
    list_display =  ('appname','get_app_url','team_name','application_username','os_type','status','version',)    
    search_fields =  ('appname','application_note','deploy_note',)
    list_filter =  ('team_name','application_username','status',)

# Register your models here.
admin.site.register(ReleaseApplication,ReleaseApplicationAdmin)
