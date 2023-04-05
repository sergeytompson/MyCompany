from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Department, Worker


class DepartmentSerializer(serializers.ModelSerializer):
    workers_count = serializers.IntegerField()
    department_salary = serializers.FloatField()
    director = serializers.StringRelatedField()

    class Meta:
        model = Department
        fields = (
            "pk",
            "name",
            "director",
            "workers_count",
            "department_salary",
        )


class WorkerSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Worker
        fields = (
            "pk",
            "name",
            "photo",
            "salary",
            "age",
            "department",
        )


user_model = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> User:
        user = user_model.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = user_model
        fields = (
            "id",
            "username",
            "password",
        )
