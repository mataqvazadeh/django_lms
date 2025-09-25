from django.db import models

class SchoolYear(models.Model):
    name = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
