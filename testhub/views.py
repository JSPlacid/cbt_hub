from testhub.models import Question
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
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


# view func for author crud


class QuestionCreate(PermissionRequiredMixin, CreateView):
    model = Question
    fields = [
        'text'
    ]


class QuestionUpdate(PermissionRequiredMixin, CreateView):
    model = Question
    fields = '__all__'


class QuestionCreate(PermissionRequiredMixin, CreateView):
    model = Question
    success_url = reverse_lazy('questions')
