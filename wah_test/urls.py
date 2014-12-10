from django.conf.urls import patterns, url, include
from wah_test import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkin/$', views.CheckInView.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/me/$', views.CurrentUserDetail.as_view()),
    url(r'^users/(?P<id>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^location/$', views.Location.as_view()),
    url(r'^occupancy/$', views.Occupancy.as_view()),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^authenticate', include('rest_framework.urls',
                                    namespace='rest_framework')),
]
