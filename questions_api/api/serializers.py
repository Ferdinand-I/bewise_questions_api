"""Модуль с сериализаторами данных."""
from rest_framework import serializers

from .models import Question
from .validators import positive_integer_validator


class QuestionsCountSerializer(serializers.Serializer):
    """Сериализатор для проверки данных в POST-запросе."""
    questions_num = serializers.IntegerField(
        validators=[positive_integer_validator]
    )


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор данных модели Question."""
    class Meta:
        model = Question
        fields = '__all__'
