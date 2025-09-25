from django.db import models

class School(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    phone = models.TextField(max_length=20)
    manager_name = models.TextField(max_length=250)
    robotic_manager_name = models.TextField(max_length=250, null=True, blank=True)