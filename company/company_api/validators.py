from django.core.exceptions import ValidationError


def validate_not_too_old(age: int) -> None:
    if age > 100:
        raise ValidationError("Сотрудник слишком старый, отпустите его на пенсию")


def validate_positive_float(num: float) -> None:
    if num < 0:
        raise ValidationError("К сожалению, мы не можем требовать с него денег")
