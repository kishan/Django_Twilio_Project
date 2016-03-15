# urls.py
 
from django.conf.urls import patterns, include, url
 
from django.contrib import admin
admin.autodiscover()

 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtwilio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
 
    # Here we add our Twilio URLs
    url(r'^', include('twilio_app.urls')),
)