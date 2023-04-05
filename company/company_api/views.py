from django.db.models import Count, Sum
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters import rest_framework as filters

from .models import Department, Worker
from .serializers import (DepartmentSerializer, RegistrationSerializer,
                          WorkerSerializer)


class WorkerPagination(PageNumberPagination):
    page_size = 5


class WorkerFilterSet(filters.FilterSet):
    department_id = filters.NumberFilter(field_name="department")
    surname = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Worker
        fields = ()


class DepartmentViewSet(ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.annotate(
        workers_count=Count("worker"),
        department_salary=Sum("worker__salary")
    )


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = WorkerPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WorkerFilterSet


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
