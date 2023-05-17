import requests


def get_questions_json(count: int, url='https://jservice.io/api/random'):
    """Добывает JSON-данные викторины с открытого API.
    Count - количество запрашиваемых элементов в массиве данных ответа.
    """
    params = {'count': count}  # параметры запроса
    response = requests.get(url=url, params=params)
    return response.json()
