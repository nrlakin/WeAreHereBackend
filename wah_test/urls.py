from django.conf.urls import patterns, url
from wah_test import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/$', views.Location.as_view()),
    url(r'^occupancy/$', views.Occupancy.as_view()),
    url(r'^update/(?P<id>[0-9]+)/$', views.Update.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login')
]
