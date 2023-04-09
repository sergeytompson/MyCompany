from django.db.models import Count, Sum, Avg, Window, F, Prefetch
from django_filters import rest_framework as filters
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Department, Worker
from .serializers import (DepartmentListSerializer, RegistrationSerializer,
                          WorkerListSerializer, WorkerRetrieveSerializer,
                          WorkerCreateSerializer, WorkerUpdateSerializer,
                          WorkerDeleteSerializer, DepartmentRetrieveSerializer,)
from .mixins import ActionsMapMixin, SERIALIZER_KEY, QUERYSET_KEY


class WorkerPagination(PageNumberPagination):
    page_size = 5


class WorkerFilterSet(filters.FilterSet):
    department_id = filters.NumberFilter(field_name="department")
    surname = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Worker
        fields = ()


class DepartmentViewSet(ActionsMapMixin, ReadOnlyModelViewSet):
    actions_map = {
        "list": {
            SERIALIZER_KEY: DepartmentListSerializer,
            QUERYSET_KEY: Department.objects.annotate(
                workers_count=Count("workers"),
                department_salary=Sum("workers__salary")
            ).select_related("director")
        },
        "retrieve": {
            SERIALIZER_KEY: DepartmentRetrieveSerializer,
            QUERYSET_KEY: Department.objects.select_related("director").prefetch_related(
                Prefetch(
                    "workers", queryset=Worker.objects.exclude(
                        pk__in=Department.objects.values_list("director", flat=True)
                    )
                )
            ),
        },
    }


class WorkerViewSet(ActionsMapMixin, ModelViewSet):
    permission_classes = (IsAuthenticated,)
    pagination_class = WorkerPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WorkerFilterSet
    actions_map = {
        "list": {
            SERIALIZER_KEY: WorkerListSerializer,
            QUERYSET_KEY: Worker.objects.annotate(
                avg_salary=Window(expression=Avg('salary'),
                                  partition_by=[F('department')]
                                  )).order_by("pk"),
        },
        "retrieve": {
            SERIALIZER_KEY: WorkerRetrieveSerializer,
            QUERYSET_KEY: Worker.objects.select_related('department'),
        },
        "partial_update": {
            SERIALIZER_KEY: WorkerUpdateSerializer,
            QUERYSET_KEY: Worker.objects.all(),
        },
        "update": {
            SERIALIZER_KEY: WorkerUpdateSerializer,
            QUERYSET_KEY: Worker.objects.all(),
        },
        "create": {
            SERIALIZER_KEY: WorkerCreateSerializer,
            QUERYSET_KEY: Worker.objects.all(),
        },
        "destroy": {
            SERIALIZER_KEY: WorkerDeleteSerializer,
            QUERYSET_KEY: Worker.objects.all(),
        },
    }


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
