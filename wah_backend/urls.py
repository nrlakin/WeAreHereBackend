from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import wah_test.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wah_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', wah_test.views.index, name='index'),
    url(r'^db', wah_test.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
)
