from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionsCountSerializer, QuestionSerializer
from .utils import get_questions_json, write_questions_to_db


class QuestionAPIView(APIView):
    """Принимает в теле запроса валидный JSON вида:
    {"questions_num": integer}, получает данные с открытого API,
    сохраняя их в БД.
    """
    http_method_names = ['post']

    def post(self, request):
        """Вью-метод для POST-запроса."""
        data = request.data
        # добываем заранее последний сохранённый объект, чтобы вернуть его
        the_last_object = Question.objects.last()
        # сериализация данных
        serializer = QuestionsCountSerializer(data=data)
        # валидация входящих данных
        if serializer.is_valid():
            count = serializer.validated_data.get('questions_num')
            # получаем данные из открытого API
            json = get_questions_json(count)
            if json:
                # записываем уникальные вопросы в БД
                write_questions_to_db(json, count)
                # метод .last() возвращает последний сохранённый объект,
                # в случае, если его нет, то он возвращает пустой объект
                # с пустыми полями
                return Response(
                    QuestionSerializer(the_last_object).data,
                    status=status.HTTP_201_CREATED)
            return Response(
                'Не удалось получить данные от внешнего сервера.',
                status=status.HTTP_404_NOT_FOUND)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)
