from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    autoload = models.BooleanField(default=True)
