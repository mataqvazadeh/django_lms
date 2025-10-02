from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsEducationEmployee
from teacher_management.models import Teacher
from teacher_management.serializer import TeacherSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes= [IsAuthenticated, IsEducationEmployee]