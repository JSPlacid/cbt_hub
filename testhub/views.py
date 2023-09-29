from django.shortcuts import render, redirect
from . models import Question, Answer
# Create your views here.


def index(request):
    """
    view function for our site's homepage
    """
    # genrate count information for questions
    queryset = Question.objects.all()
    # ans = Answer.objects.all()
    # context = {
    #    'queryset': queryset,
    #    'options': ans
    # }

    # render html template index.html with context data
    return render(request, 'index.html', {'questions': queryset})
