from rest_framework.serializers import ModelSerializer

from teacher_management.models import SessionReport, Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ReportSerializer(ModelSerializer):
    class Meta:
        model = SessionReport
        fields = '__all__'
        read_only_fields = [
            'teacher',
            'status',
            'is_verified',
            'created_at',
            'updated_at',
        ]
