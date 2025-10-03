from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from accounts.permissions import IsTeacher, IsEducationEmployee
from teacher_management.models import SessionReport
from teacher_management.serializer import ReportSerializer

class ReportViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = SessionReport.objects.all()
    serializer_class = ReportSerializer

    def get_permissions(self):
        if self.action in {'create'}:
            return [IsTeacher()]
        elif self.action in {'retrieve', 'list'}:
            return [(IsEducationEmployee | IsTeacher)()]

    def get_queryset(self):
        if self.request.user.teacher:
            return self.queryset.filter(teacher=self.request.user.teacher)
        else:
            return self.queryset.all()
        
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['teacher_id'] = self.request.user.teacher.pk
        return context