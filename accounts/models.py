from django.db import models
from django.conf import settings

class UserRoles(models.Model):
    class Roles(models.IntegerChoices):
        Secretary = 1, "منشی"
        EducationManager = 2
        EducationEmployee = 3
        FinancialManager = 4
        FinancialEmployee = 5
        Teacher = 6, "مربی"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=Roles.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'role'), name='uix_userroles_user_role')
        ]

    def __str__(self):
        return f'{self.user.get_full_name()}, {self.get_role_display()}'