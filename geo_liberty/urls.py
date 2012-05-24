from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import upload

admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^admin/', include(admin.site.urls)),
     url(r'^upload/$',upload),
     url(r'^chaining/', include('smart_selects.urls')),
)
