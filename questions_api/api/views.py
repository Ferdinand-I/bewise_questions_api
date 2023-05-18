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
    http_method_names = ['get', 'post']

    def get(self, request):
        data = QuestionSerializer(Question.objects.all(), many=True).data
        return Response(data)

    def post(self, request):
        """Вью-метод для POST-запроса."""
        data = request.data
        # добываем заранее последний сохранённый объект, чтобы вернуть его
        the_last_object = Question.objects.last()
        # валидация входящих данных
        if QuestionsCountSerializer(data=data).is_valid():
            count = data.get('questions_num')
            json = get_questions_json(count)
            write_questions_to_db(json, count)
            # метод .last() возвращает последний сохранённый объект,
            # в случае, если его нет, то он возвращает пустой объект
            # с пустыми полями
            return Response(
                QuestionSerializer(the_last_object).data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            'Что-то пошло не так...', status=status.HTTP_400_BAD_REQUEST
        )
