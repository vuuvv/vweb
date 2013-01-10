from django.db import models

class SMSContent(models.Model):
    content = models.TextField()

class SMSLog(models.Model):
    phone = models.CharField(max_length=255)
    content = models.ForeignField(SMSContent)
    status = models.CharField(max_length=255)
    request_at = models.DatetimeField()
    send_at = models.DatetimeField()
