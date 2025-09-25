from django.db import models
from django.contrib.auth.models import User

class UserRoles(models.Model):
    class Roles(models.IntegerChoices):
        Secretary = 1
        EducationManager = 2
        EducationEmployee = 3
        FinancialManager = 4
        FinancialEmployee = 5
        Teacher = 6

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=Roles.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'role'), name='uix_userroles_user_role')
        ]