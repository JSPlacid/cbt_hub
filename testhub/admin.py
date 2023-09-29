from django.contrib import admin
from .models import Question, Answer

# Register your models here.


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """class for answer model"""
    list_display = ('text', 'question', 'is_correct')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """class for question model"""
    list_display = ['text']
