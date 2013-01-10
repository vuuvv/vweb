from django.conf.urls import patterns, include, url

from vweb.dashboard.views import Main, Login, SMS

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='main'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^sms/$', SMS.as_view(), name='sms'),
)
