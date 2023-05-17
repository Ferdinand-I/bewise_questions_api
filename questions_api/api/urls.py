from .views import QuestionAPIView
from django.urls import path


urlpatterns = [
    path('questions/', QuestionAPIView.as_view()),
]
