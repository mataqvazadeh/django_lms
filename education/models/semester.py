from django.db import models
from education.models import SchoolYear

class Semester(models.Model):
    class SemesterType(models.IntegerChoices):
        Term1= 1, 'ترم 1'
        Term2= 2, 'ترم 2'
        Summer= 3, 'ترم تابستانی'

    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    tp = models.PositiveSmallIntegerField(choices=SemesterType.choices)

    @property
    def name(self):
        return f'{self.get_tp_display()} {self.school_year.name}'

    def __str__(self):
        return self.name
