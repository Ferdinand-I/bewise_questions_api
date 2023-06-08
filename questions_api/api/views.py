from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionsCountSerializer, QuestionSerializer
from .utils import sync_remote_questions


class QuestionAPIView(APIView):
    """Принимает в теле запроса валидный JSON вида:
    {"questions_num": integer}, получает данные с открытого API,
    сохраняя их в БД.
    """
    http_method_names = ['post']

    def post(self, request):
        """Вью-метод для POST-запроса."""
        data = request.data
        # сериализация данных
        serializer = QuestionsCountSerializer(data=data)
        # валидация входящих данных
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        last_saved_object_data = QuestionSerializer(
            Question.objects.last()).data
        count = serializer.validated_data.get('questions_num')
        return sync_remote_questions(count, last_saved_object_data)
