import re
from datetime import datetime

from django.core import serializers
from django.forms.models import modelform_factory
from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

from vweb.utils.views import View
from vweb.utils.serialize import tojson, model_to_dict
from vweb.sms.models import SMSLog, SMSContent

class Login(View):
    template_name = "dashboard/login.html"

class Main(View):
    template_name = "dashboard/main.html"

class Textarea(widgets.Widget):
    def __init__(self, attrs=None):
        default_attrs = {'rows': '3', 'class': 'input-xxlarge'}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))

class SMSSendForm(forms.Form):
    phones = forms.CharField(label=_("phone"), widget=Textarea)
    content = forms.CharField(label=_("content"), widget=Textarea)
    priority = forms.ChoiceField(label=_("priority"), initial=SMSLog.NORMAL, choices=SMSLog.PRIORITY_CHOICES)
    request_at = forms.DateTimeField(label=_("request at"), initial=datetime.now)

    def clean_phones(self):
        return re.split('[^0-9\-]+', self.cleaned_data["phones"])

class SMSList(View):
    template_name = "dashboard/sms_list.html"

    def get_context_data(self, **kwargs):
        smslist = SMSLog.objects.all().order_by("status", "-request_at", "priority")
        return {
            "smslist": smslist
        }

class SMSSend(View):
    template_name = "dashboard/sms_send.html"

    def post(self, request):
        form = SMSSendForm(request.POST)
        if form.is_valid():
            content = SMSContent(content=form.cleaned_data["content"])
            content.save()
            for phone in form.cleaned_data["phones"]:
                log = SMSLog(
                    phone = phone,
                    content = content,
                    status = SMSLog.REQUEST,
                    priority = form.cleaned_data["priority"],
                    request_at = form.cleaned_data["request_at"]
                )
                log.save()
            return HttpResponse("OK")
        else:
            return HttpResponse(form.errors)

class SMSPull(View):
    def get(self, request):
        max_count = int(request.GET.get("max_count", 10))
        sms = SMSLog.objects.select_related().filter(
            status=SMSLog.REQUEST, request_at__lte=datetime.now()
        ).order_by(
            'priority', 'request_at'
        )[:max_count]
        resp = tojson([model_to_dict(m, ["id", "phone", "content.content"]) for m in sms])
        for s in sms:
            s.status = SMSLog.SENDING
            s.save()
        return HttpResponse(resp)

class SMSSended(View):
    def post(self, request):
        sms = json.loads(request.POST["sms"])
        for s in sms:
            model = SMSLog.objects.get(pk=s.id)
            model.status = SMSLog.SUCCESS
            model.save()
        return HttpResponse("OK")

