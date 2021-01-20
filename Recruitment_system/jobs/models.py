
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
JobTypes = [
    (0, "������"),
    (1, "��Ʒ��"),
    (2, "��Ӫ��"),
    (3, "�����"),
    (4, "�г�Ӫ����")
]
Cities = [
    (0, "����"),
    (1, "�Ϻ�"),
    (2, "����"),
    (3, "����"),
    (4, "����")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="ְλ�б�")
    job_name = models.CharField(max_length=250, blank=False, verbose_name="ְλ����")
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name="�����ص�")
    job_responsibility = models.TextField(max_length=1024, verbose_name="ְλְ��")
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name="ְλҪ��")
    creator = models.ForeignKey(User, verbose_name="������", on_delete=None)  # �������
    created_date = models.DateTimeField(verbose_name="��������")
    modified_date = models.DateTimeField(verbose_name="�޸�ʱ��")