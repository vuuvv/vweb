from vweb.utils.views import View
from django.forms.models import modelform_factory
from vweb.sms.models import SMSLog

class Login(View):
    template_name = "dashboard/login.html"

class Main(View):
    template_name = "dashboard/main.html"

class SMS(View):
    template_name = "dashboard/sms.html"

class SMSSendForm(Form):
    phones = forms.TextField()
    content = forms.TextField()

class SMSSend(View):
    template_name = "dashboard/sms_send.html"

    def post(self, request):
        phones = request.POST.phones
        content = request.POST.content

