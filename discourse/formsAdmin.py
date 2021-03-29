from django.forms import ModelForm
from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class createSchedule(ModelForm):
    class Meta:
        model = models.schedule
        fields = ['date', 'time', 'lector', 'topic', 'description', 'link', 'tag']
        widgets = {
            'date': DateInput(),
        }
