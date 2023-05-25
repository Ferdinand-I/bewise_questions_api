from django.db import models


class Question(models.Model):
    """Модель вопросов."""
    question_id = models.IntegerField(verbose_name='ID вопроса', unique=True)
    text = models.TextField(verbose_name='Текст вопроса')
    answer = models.CharField(verbose_name='Ответ на вопрос', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата создания вопроса')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.question_id)
