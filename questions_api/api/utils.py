"""Модуль с утилитами."""
import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Question


def sync_remote_questions(count: int, last_object_data: ReturnDict):
    """Добываем удалённые записи вопросов для викторины и записываем в БД."""
    # добываем данные с удалённого API
    url = settings.REMOTE_URL
    params = {'count': count}
    response = requests.get(url, params)
    if not response.ok:
        return Response(
            'Получен некорректный ответ от удалённого сервера.',
            status=response.status_code)
    json = response.json()
    # Делаем один SQL-запрос, чтобы выгрузить все 'questions_id' для сравнения
    ids = Question.objects.values_list('question_id', flat=True)
    to_insert = [
        Question(
            question_id=question.get('id'),
            text=question.get('question'),
            answer=question.get('answer'),
            created_at=question.get('created_at')
        ) for question in json if question.get('id') not in ids
    ]
    # сохраняем уникальные объекты в БД
    inserted = Question.objects.bulk_create(to_insert)
    length_inserted = len(inserted)
    # Если мы не получили достаточно уникальных объектов,
    # то делаем новый удалённый запрос
    if length_inserted != count:
        return sync_remote_questions(count - length_inserted, last_object_data)
    return Response(last_object_data, status=status.HTTP_201_CREATED)
