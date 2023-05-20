"""Модуль с валидаторами полей сериализаторов."""
from rest_framework.validators import ValidationError


def positive_integer_validator(value: int):
    """Функция-валидатор, которая проверяет, является ли значение поля
    с типом данных Integer больше нуля.
    """
    if value < 1:
        raise ValidationError()