from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from accounts.serializers import UserSerializer
from accounts.models import UserRoles
from teacher_management.models import SessionReport, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        first_name = validated_data['user']['first_name']
        last_name = validated_data['user']['last_name']
        username = validated_data['user']['username']
        password = validated_data['user']['password']

        with transaction.atomic():
            teacher_user = get_user_model().objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            teacher_user.roles.create(role=UserRoles.Roles.Teacher)

            return Teacher.objects.create(
                user=teacher_user,
                phone=validated_data['phone'],
                emergency_phone=validated_data['emergency_phone'],
            )


class ReportSerializer(serializers.ModelSerializer):
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
