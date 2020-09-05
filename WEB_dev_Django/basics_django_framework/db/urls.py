from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_test/$', views.test_create),
]