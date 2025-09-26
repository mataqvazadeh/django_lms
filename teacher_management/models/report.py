from django.db import models


class SessionReport(models.Model):
    class States(models.IntegerChoices):
        SUBMITTED = 1
        ACCEPTED = 2
        UNACCEPTED = 3

    teacher = models.ForeignKey('teacher_management.Teacher', on_delete=models.PROTECT)
    klass = models.ForeignKey('education.Klass', on_delete=models.PROTECT)
    date = models.DateField()
    report = models.TextField()
    students = models.JSONField()
    status = models.PositiveSmallIntegerField(
        choices=States.choices, default=States.SUBMITTED
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('teacher', 'klass', 'date'),
                name='uix_sessionreport_teacher_klass_date',
            ),
            models.UniqueConstraint(
                fields=('klass', 'date'),
                name='uix_sessionreport_klass_date',
            )
        ]