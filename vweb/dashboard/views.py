from vweb.utils.views import View

class Login(View):
    template_name = "dashboard/login.html"

class Main(View):
    template_name = "dashboard/main.html"

class SMS(View):
    template_name = "dashboard/sms.html"
