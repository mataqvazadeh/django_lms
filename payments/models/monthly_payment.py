from django.db import models


class MonthlyPayment(models.Model):
    teacher = models.ForeignKey('teacher_management.Teacher', on_delete=models.CASCADE)
    month = models.DateField()
    salary = models.DecimalField(max_digits=18, decimal_places=6)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('teacher', 'month'),
                name='uix_monthlypayment_teacher_month',
            )
        ]
