from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from accounts.models import UserRoles
from teacher_management.models import SessionReport, Teacher


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField()
    emergency_phone = serializers.CharField()

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        password = validated_data['password']

        with transaction.atomic():
            user_model = get_user_model()

            teacher_user = user_model.objects.filter(username=username).first()
            if not teacher_user:
                teacher_user = user_model.objects.create_user(
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

    def to_representation(self, instance: Teacher):
        result = {}
        result['id'] = instance.id
        result['first_name'] = instance.user.first_name
        result['last_name'] = instance.user.last_name
        result['username'] = instance.user.username
        result['phone'] = instance.phone
        result['emergency_phone'] = instance.emergency_phone

        return result

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

    def create(self, validated_data):
        validated_data['teacher_id'] = self.context['teacher_id']
        return super().create(validated_data)