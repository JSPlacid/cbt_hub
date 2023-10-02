from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_questions/<int:question_id>/', views.get_questions, name='get_questions'),
    path('review_quiz/', views.review_quiz, name='review_quiz'),
    path('instruction/', views.instruction, name='instruction'),
]
