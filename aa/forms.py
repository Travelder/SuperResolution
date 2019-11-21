from .models import Process
from django import forms

class ProcessForm(forms.ModelForm):
    class Meta:
        model=Process
        exclude=()