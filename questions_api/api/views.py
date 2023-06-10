from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QuestionsCountSerializer
from .utils import collect_and_save_unique_objects


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
        count = serializer.validated_data.get('questions_num')
        return collect_and_save_unique_objects(count)
