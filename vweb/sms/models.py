from django.db import models
from django.utils.translation import ugettext_lazy as _

class SMSContent(models.Model):
    content = models.TextField(_("content"))

class SMSLog(models.Model):
    REQUEST = 'REQUEST'
    SENDING = 'SENDING'
    FAILED = 'FAILED'
    SUCCESS = 'SUCCESS'
    STATUS_CHOICES = (
        (REQUEST, _("Request")),
        (SENDING, _("Sending")),
        (FAILED, _("Failed")),
        (SUCCESS, _("Success")),
    )

    phone = models.CharField(_("phone"), max_length=255)
    content = models.ForeignKey(SMSContent, verbose_name=_("content"))
    status = models.CharField(_("status"), max_length=255, choices=STATUS_CHOICES)
    request_at = models.DateTimeField(_("request at"), auto_now_add=True, blank=True)
    send_at = models.DateTimeField(_("send_at"), blank=True)
