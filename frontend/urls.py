from django.conf.urls import patterns, url
from test_frontend import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
