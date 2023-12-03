from django import forms
from .models import Answer

class AnswerForm(forms.Form):
    answer = forms.ModelChoiceField(queryset=Answer.objects.all(), widget=forms.RadioSelect, empty_label=None)