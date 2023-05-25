"""Модуль с сериализаторами данных."""
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Question


class QuestionsCountSerializer(serializers.Serializer):
    """Сериализатор для проверки данных в POST-запросе."""
    questions_num = serializers.IntegerField()

    def validate_questions_num(self, value: int):
        """Валидация поля 'questions_num'."""
        if value < 1:
            raise ValidationError(
                'Значение "questions_num" должно быть больше 0.')
        return value


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор данных модели Question."""
    class Meta:
        model = Question
        fields = '__all__'
