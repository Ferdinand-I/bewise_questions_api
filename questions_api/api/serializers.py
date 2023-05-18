from rest_framework import serializers
from .models import Question


class QuestionsCountSerializer(serializers.Serializer):
    """Сериализатор для проверки данных в POST-запросе."""
    questions_num = serializers.IntegerField()


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
