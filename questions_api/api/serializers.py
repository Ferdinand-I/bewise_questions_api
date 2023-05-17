from rest_framework import serializers


class QuestionsCountSerializer(serializers.Serializer):
    """Сериализатор для проверки данных в POST-запросе."""
    questions_num = serializers.IntegerField()
