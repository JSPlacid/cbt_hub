from django.shortcuts import render
from .models import Question, Answer
from django.http import JsonResponse
import requests


# Create your views here.
def index(request):
    """View function for home page"""

    return (render(request, 'index.html'))


# save the questions and answerns in json format
def get_questions_json(request):
    questions = Question.objects.all()
    data = []
    for question in questions:
        answers = Answer.objects.filter(question=question)
        question_data = {
            'question': question.text,
            'answers': [{'text': answer.text} for answer in answers]
        }
        data.append(question_data)

    return JsonResponse({'data': data})

# loop throught the json data


def display_quiz(request):
    response = requests.get('http://localhost:7000/testhub/get_questions_json')

    if response.status_code == 200:
        data = response.json()['data']
        return (render(request, 'quiz.html', {'data': data}))

    else:
        return JsonResponse({'Error': 'failed to fetch quiz data'}, status=500)
