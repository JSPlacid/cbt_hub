from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_questions_json/', views.get_questions_json, name='get_questions_json'),
    path('display_quiz/', views.display_quiz, name='display_quiz'),
]
