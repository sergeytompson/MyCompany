from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Department, Worker
from .serializers import (DepartmentSerializer, RegistrationSerializer,
                          WorkerSerializer)


class WorkerPagination(PageNumberPagination):
    page_size = 5


class DepartmentViewSet(ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class WorkerViewSet(ModelViewSet):
    serializer_class = WorkerSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = WorkerPagination

    def get_queryset(self) -> QuerySet:
        department_filter = "department_id"
        surname_filter = "surname"
        queryset = Worker.objects.all()
        if department_filter in self.request.query_params:
            queryset = queryset.filter(
                department=self.request.query_params[department_filter]
            )
        if surname_filter in self.request.query_params:
            queryset = queryset.filter(
                name__contains=self.request.query_params[surname_filter]
            )
        return queryset


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
