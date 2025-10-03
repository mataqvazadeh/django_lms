from django.contrib import admin
from education import models
# Register your models here.
admin.site.register(models.SchoolYear)
admin.site.register(models.Semester)
admin.site.register(models.School)
admin.site.register(models.Klass)