from django.db import models

from .validators import validate_not_too_old, validate_positive_float


class Department(models.Model):
    name = models.CharField("Название департамента", max_length=150)
    director = models.OneToOneField(
        "Worker",
        models.SET_NULL,
        verbose_name="Директор департамента",
        related_name="department_director",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"


class Worker(models.Model):
    last_name = models.CharField("Фамилия", max_length=150, default="Фамилия")
    first_name = models.CharField("Имя", max_length=150, default="Имя")
    patronymic = models.CharField("Отчество", max_length=150, blank=True, null=True)
    photo = models.ImageField("Фото", upload_to="workers/", blank=True, null=True)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Оклад",
        validators=(validate_positive_float,),
    )
    age = models.PositiveIntegerField("Возраст", validators=(validate_not_too_old,))
    department = models.ForeignKey(
        Department,
        models.SET_NULL,
        verbose_name="Департамент",
        null=True,
        blank=True,
        related_name="workers",
    )

    def __str__(self) -> str:
        patronymic_or_empty_line = f" {self.patronymic}" if self.patronymic else ""
        return f"{self.last_name} {self.first_name}{patronymic_or_empty_line}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
