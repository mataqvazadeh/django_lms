from django.db import models


class BaseSalary(models.Model):
    teacher = models.ForeignKey('teacher_management.Teacher', on_delete=models.CASCADE)
    school_year = models.ForeignKey('education.SchoolYear', on_delete=models.PROTECT)
    salary = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f'{self.teacher.user.get_full_name()} - {self.school_year.name} - {self.salary}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('teacher', 'school_year'),
                name='uix_basesalary_teacher_school_year',
            )
        ]
