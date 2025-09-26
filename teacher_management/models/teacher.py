from django.db import models
from django.conf import settings


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.TextField(max_length=20)
    emergency_phone = models.TextField(max_length=20)
