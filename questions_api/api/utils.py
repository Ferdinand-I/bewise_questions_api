"""Модуль с утилитами."""
import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


def collect_and_save_unique_objects(count: int):
    """Собирает уникальные объекты с удалённого сервера
    и записывает их в БД.
    """
    # список существующих id вопросов в БД
    ids = set(Question.objects.values_list('question_id', flat=True))
    url = settings.REMOTE_URL
    unique_objects_to_insert = list()
    last_saved_object_data = QuestionSerializer(Question.objects.last()).data

    while count > 0:
        params = {'count': count}
        response = requests.get(url, params)
        if not response.ok:
            return Response(
                'Получен некорректный ответ от удалённого сервера.',
                status=response.status_code)

        json = response.json()
        unique_objects = [
            Question(
                question_id=question.get('id'),
                text=question.get('question'),
                answer=question.get('answer'),
                created_at=question.get('created_at')
            ) for question in json if question.get('id') not in ids
        ]
        unique_objects_to_insert.extend(unique_objects)
        ids.update(
            (question.question_id for question in unique_objects_to_insert)
        )
        count -= len(unique_objects)

    # На случай параллельных запросов к БД ставим флаг ignore_conflicts=True
    inserted = Question.objects.bulk_create(
        unique_objects_to_insert, ignore_conflicts=True)
    response_data = {
        'count_new_questions': len(inserted),
        'last_saved_question': last_saved_object_data
    }
    return Response(response_data, status=status.HTTP_201_CREATED)
