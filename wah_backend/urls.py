from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
     url(r'^', include('wah_test.urls')),
     url(r'^test/', include('frontend.urls'))
]
"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wah_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', wah_test.views.WAH_Test.as_view().index, name='index'),
    #url(r'^db', wah_test.views.as_view().db, name='db'),
    #url(r'^$', wah_test.views.WAH_Test.as_view(), name='api')
    url(r'^', include(wah_test.urls))
    #url(r'^admin/', include(admin.site.urls)),
)
"""
