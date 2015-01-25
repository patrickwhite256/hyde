from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hyde.views.home', name='home'),
    url(r'^$', include('hyde_web.urls')),
    # url(r'^blog/', include('blog.urls')),
)
