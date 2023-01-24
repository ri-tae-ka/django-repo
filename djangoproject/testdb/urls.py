from django.urls import re_path
from testdb import views

urlpatterns = [
    re_path(r'^user', views.userAPI),
]