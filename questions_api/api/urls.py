from django.urls import path

from .views import QuestionAPIView

urlpatterns = [
    path('questions/', QuestionAPIView.as_view()),
]
