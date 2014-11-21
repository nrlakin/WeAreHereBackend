from django.conf.urls import patterns, url
from wah_test import views

urlpatterns = [
    url(r'^occupancy/$', views.occupancy),
    url(r'^update/(?P<id>[0-9]+)/$', views.update),
]
