from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Question(models.Model):
    """class model for questions"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)

    def __str__(self):
        """String representation for Question model"""
        return self.text


class Answer(models.Model):
    """class model for answer"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        """String representation for Answer model"""
        return self.text


class UserResponse(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'User: {self.user.username}, Question: {self.question.text}, correct: {self.is_correct}'
