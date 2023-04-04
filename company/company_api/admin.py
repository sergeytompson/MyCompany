from django.contrib import admin

from .models import Department, Worker


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    list_display_links = (
        "pk",
        "name",
    )
    search_fields = ("name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "department")
    list_display_links = (
        "pk",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("department",)
