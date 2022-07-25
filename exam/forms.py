from django import forms 
from .models import Course,Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question','option1','option2','option3','option4','marks','answer']