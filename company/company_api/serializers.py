from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Department, Worker


class DepartmentListSerializer(serializers.ModelSerializer):
    workers_count = serializers.IntegerField()
    department_salary = serializers.FloatField()
    director = serializers.CharField()

    class Meta:
        model = Department
        fields = (
            "pk",
            "name",
            "director",
            "workers_count",
            "department_salary",
        )


class WorkerSerializerForDepartmentRetrieve(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = ("pk", "name", "salary", "age",)

    def get_name(self, obj):
        return Worker.get_worker_name(obj)


class DepartmentRetrieveSerializer(serializers.ModelSerializer):
    workers = WorkerSerializerForDepartmentRetrieve(many=True, read_only=True)
    director = WorkerSerializerForDepartmentRetrieve(read_only=True)

    class Meta:
        model = Department
        fields = (
            "pk",
            "name",
            "director",
            "workers"
        )


class DepartmentSerializerForWorkerRetrieve(serializers.ModelSerializer):
    director = serializers.CharField()

    class Meta:
        model = Department
        fields = (
            "pk",
            "name",
            "director",
        )


class WorkerListSerializer(serializers.ModelSerializer):
    avg_salary = serializers.FloatField()
    department = serializers.CharField()

    class Meta:
        model = Worker
        fields = (
            "pk",
            "last_name",
            "first_name",
            "patronymic",
            "avg_salary",
            "photo",
            "salary",
            "age",
            "department",
        )


class WorkerRetrieveSerializer(serializers.ModelSerializer):
    department = DepartmentSerializerForWorkerRetrieve(read_only=True)

    class Meta:
        model = Worker
        fields = (
            "last_name",
            "first_name",
            "patronymic",
            "photo",
            "salary",
            "age",
            "department",
        )


class WorkerChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ("last_name", "first_name", "patronymic", "salary", "age", "department",)


class WorkerCreateSerializer(WorkerChangeSerializer):
    pass


class WorkerUpdateSerializer(WorkerChangeSerializer):
    pass


class WorkerDeleteSerializer(WorkerChangeSerializer):
    pass


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
