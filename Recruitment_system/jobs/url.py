from django.conf.urls import url
from jobs import views


urlpatterns = [
    # ְλ�б�
    url(r"^joblist/", views.joblist, name="joblist")
]