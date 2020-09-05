from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'simple_route', views.simple_route),
    url(r'slug_route/(?P<slug>[0-9|a-z\-|_]{1,16})/', views.slug_route),
    url(r'sum_route/(?P<var_1>-?\d{1,5})/(?P<var_2>-?\d{1,5})/', views.sum_route),
    url(r'sum_get_method/', views.get_sum_route),
    url(r'sum_post_method/', views.sum_post_method),
]
