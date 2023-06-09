"""Тесты сериализаторов."""
from random import randint

from django.test.testcases import TestCase

from ..serializers import QuestionsCountSerializer


class QuestionsCountSerializerTests(TestCase):
    """Тесты QuestionsCountSerializer."""
    def test_validation_suscess(self):
        """Тест успешной валидации."""
        random_valid_count = randint(1, 10)
        python_valid_data = {'questions_num': random_valid_count}
        serializer = QuestionsCountSerializer(data=python_valid_data)
        self.assertTrue(serializer.is_valid())

    def test_validation_error(self):
        """Тест ошибки валидации."""
        random_invalid_count = randint(-10, 0)
        python_invalid_data = {'questions_num': random_invalid_count}
        serializer = QuestionsCountSerializer(data=python_invalid_data)
        self.assertFalse(serializer.is_valid())
