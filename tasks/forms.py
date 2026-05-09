from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
      model=Task
      fields=["task"]
      widgets = {
            "task":forms.TextInput(attrs={
                "placeholder": "Create a new task..."
            }),
        }