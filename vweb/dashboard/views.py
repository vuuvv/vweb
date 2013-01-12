import datetime

from django.forms.models import modelform_factory
from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _

from vweb.utils.views import View
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
    request_at = forms.DateTimeField(label=_("request at"), initial=datetime.datetime.now)

    def clean_phones(self):
        return self.cleaned_data['phones'].split(",")

class SMS(View):
    template_name = "dashboard/sms.html"

    def get_context_data(self, **kwargs):
        form = SMSSendForm()
        return {
            "form": form,
        }

class SMSSend(View):
    template_name = "dashboard/sms_send.html"

    def get_context_data(self, **kwargs):
        form = SMSSendForm(request.POST)
        return {
            "form": form,
        }

    def post(self, request):
        from django.http import HttpResponse
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

