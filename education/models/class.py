from django.db import models

from teacher_management.models import Teacher


class Klass(models.Model):
    class KlassTime(models.IntegerChoices):
        MIN60 = 60
        MIN90 = 90
        MIN120 = 120

    name = models.CharField(max_length=250)
    school = models.ForeignKey('School', on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    time = models.SmallIntegerField(choices=KlassTime.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    teachers = models.ManyToManyField(
        Teacher, through='KlassTeacher', through_fields=('klass', 'teacher')
    )
    assistants = models.ManyToManyField(
        Teacher,
        null=True,
        through='KlassAssistant',
        through_fields=('klass', 'teacher'),
    )

    def __str__(self):
        return f'{self.name} - {self.school.name} - {self.semester}'


class KlassTeacher(models.Model):
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()


class KlassAssistant(models.Model):
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
