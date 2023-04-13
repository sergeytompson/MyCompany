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
    list_display = (
        "pk",
        "department",
        "name",
    )
    list_display_links = (
        "pk",
        "name",
    )
    search_fields = (
        "last_name",
        "first_name",
        "patronymic",
    )
    list_filter = ("department",)
    fields = (
        "last_name",
        "first_name",
        "patronymic",
        "photo",
        "salary",
        "age",
        "department",
    )

    def name(self, obj: Worker) -> str:
        return str(obj)

    name.short_description = "ФИО"
