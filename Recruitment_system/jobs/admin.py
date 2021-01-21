# coding=gbk
from django.contrib import admin
from jobs.models import Job
from jobs.models import NaMei
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    # ����ҳ����Ҫ��ʾ������
    exclude = ('creator',)
    # վ����Ŀ��ʾ����
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)
admin.site.register(NaMei)