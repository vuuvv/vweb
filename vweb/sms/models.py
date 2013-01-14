from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class SMSContent(models.Model):
    content = models.TextField(_("content"))

    def __unicode__(self):
        return u"%s" % self.content

class SMSLog(models.Model):
    REQUEST = 1
    SENDING = 2
    FAILED = 3
    SUCCESS = 4
    STATUS_CHOICES = (
        (REQUEST, _("Request")),
        (SENDING, _("Sending")),
        (FAILED, _("Failed")),
        (SUCCESS, _("Success")),
    )

    URGENCY = 1
    FATAL = 10
    NORMAL = 20
    PRIORITY_CHOICES = (
        (URGENCY, _("Urgency")),
        (FATAL, _("Fatal")),
        (NORMAL, _("Normal")),
    )

    phone = models.CharField(_("phone"), max_length=255)
    content = models.ForeignKey(SMSContent, verbose_name=_("content"))
    status = models.IntegerField(_("status"), choices=STATUS_CHOICES)
    priority = models.IntegerField(_("priority"), default=NORMAL, choices=PRIORITY_CHOICES)
    request_at = models.DateTimeField(_("request at"), default=datetime.now, blank=True)
    send_at = models.DateTimeField(_("send at"), blank=True, null=True)
    create_at = models.DateTimeField(_("create at"), auto_now_add=True)
