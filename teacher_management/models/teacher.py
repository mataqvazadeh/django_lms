from django.db import models, transaction
from django.conf import settings

from accounts.models import UserRoles


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.TextField(max_length=20)
    emergency_phone = models.TextField(max_length=20)

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            teacher_role = self.user.roles.filter(role=UserRoles.Roles.Teacher)       
            if teacher_role:
                teacher_role.delete()

            teacher_user = self.user

            result = super().delete(*args, **kwargs)

            if not teacher_user.roles.exists():
                teacher_user.delete()

            return result
