from django import forms
from .models import *


class Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['text']
        labels = {'text': ''}
