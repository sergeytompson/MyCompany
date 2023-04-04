from django.urls import include, path
from rest_framework import routers

from .views import DepartmentViewSet, RegistrationAPIView, WorkerViewSet

router = routers.SimpleRouter()
router.register(r"department", DepartmentViewSet, basename="department")
router.register(r"worker", WorkerViewSet, basename="worker")


urlpatterns = [
    path("", include(router.urls)),
    path("auth", include("rest_framework.urls", namespace="rest_framework")),
    path("registration", RegistrationAPIView.as_view(), name="registration"),
]
