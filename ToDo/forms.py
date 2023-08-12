from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  
        fields = ['title', 'description', 'date']  # Add the fields you want to include
