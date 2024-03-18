from django import forms
from .models import WorkRequest

class WorkRequestForm(forms.ModelForm):
    class Meta:
        model = WorkRequest
        fields = ['name', 'email', 'about_me', 'why_us']