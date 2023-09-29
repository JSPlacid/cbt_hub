from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    """class model for questions"""
    text = models.CharField(max_length=255)

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
