from django.conf.urls import patterns, include, url
from car import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'parking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^car/', include('car.urls')),
    url(r'^accounts/', include('allauth.urls')), 
)

