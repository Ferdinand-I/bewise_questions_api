"""Тесты Вью."""
from django.urls import reverse
from rest_framework.test import APITestCase


class QuestionViewTests(APITestCase):
    """Тесты QuestionAPIView."""
    @classmethod
    def setUpTestData(cls):
        """Фикстуры."""
        cls.url = reverse('question')
        cls.valid_input_data = '{"questions_num": 1}'
        cls.invalid_input_data = '{"questions_num": -1}'

    def test_success_post_status(self):
        """Тест усипешного post запроса."""
        response = self.client.post(
            self.url,
            data=self.valid_input_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
