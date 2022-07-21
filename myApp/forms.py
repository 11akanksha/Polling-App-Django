from django import forms
from myApp import models


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ["choice"]
