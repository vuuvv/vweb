from django.conf.urls import patterns, include, url

from vweb.dashboard.views import Main, Login, SMSList, SMSSend, SMSPull, SMSSended

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='main'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^sms/$', SMSList.as_view(), name='sms_list'),
    url(r'^sms/send$', SMSSend.as_view(), name='sms_send'),
    url(r'^sms/pull$', SMSPull.as_view(), name='sms_pull'),
    url(r'^sms/sended$', SMSSended.as_view(), name='sms_sended'),
)
