from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import QuestionsCountSerializer
from .utils import get_questions_json


class QuestionAPIView(APIView):
    """Принимает в теле запроса валидный JSON вида:
    {"questions_num": integer}, получает данные с открытого API,
    сохраняя их в БД.
    """
    http_method_names = ['post']

    def post(self, request):
        """Вью-метод для POST-запроса."""
        data = request.data
        if QuestionsCountSerializer(data=data).is_valid():
            json = get_questions_json(data.get('questions_num'))
            return Response(json)
        return Response('Что-то пошло не так...')
