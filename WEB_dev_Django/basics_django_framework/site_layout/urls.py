from django.conf.urls import url, include
from django.shortcuts import render
from .views import first_attempt

urlpatterns = [
    url(r'^1_att/$', first_attempt),
]