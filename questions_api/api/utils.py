import requests

from .models import Question


def get_questions_json(
        count: int, url: str = 'https://jservice.io/api/random'):
    """Добывает JSON-данные викторины с открытого API.
    Count - количество запрашиваемых элементов в массиве данных ответа.
    """
    params = {'count': count}  # параметры запроса
    response = requests.get(url=url, params=params)
    return response.json()


def write_questions_to_db(data_list: list, count: int):
    """Функция записи данных вопроса в БД."""
    # формируем список уникальных записей
    objects = [
        Question(
            question_id=question.get('id'),
            text=question.get('question'),
            answer=question.get('answer'),
            created_at=question.get('created_at'))
        for question in data_list
        if not Question.objects.filter(question_id=question.get('id')).exists()
    ]
    # записываем уникальные вопросы в БД
    Question.objects.bulk_create(objects)
    # если мы не набрали нужное количество уникальных записей, то сравниваем
    # количество записанных данных с ожидаемым, считаем разницу
    # и рекурсивно вызываем функцию, чтобы набрать необходимое количество
    if count > len(objects):
        count = count - len(objects)
        addition_request_json = get_questions_json(count)
        write_questions_to_db(addition_request_json, count)
    return
