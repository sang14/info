from django.conf.urls import patterns, include, url
from django.contrib import admin
from myinfo.views import index 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^myinfo/?$', index),
)
