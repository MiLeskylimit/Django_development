from django.conf.urls import url
from jobs import views


urlpatterns = [
    # ְλ�б�
    url(r"^joblist/", views.joblist, name="joblist"),
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
]