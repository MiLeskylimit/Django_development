from django.conf.urls import url
from jobs import views


urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name="joblist"),
    url(r"^jobs/(?P<job_id>\d+)/$", views.detail, name="detail"),
]