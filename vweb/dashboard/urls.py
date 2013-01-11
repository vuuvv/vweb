from django.conf.urls import patterns, include, url

from vweb.dashboard.views import Main, Login, SMS, SMSSend

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='main'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^sms/$', SMS.as_view(), name='sms'),
    url(r'^sms/send$', SMSSend.as_view(), name='sms_send'),
)
