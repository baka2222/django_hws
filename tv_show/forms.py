from django import forms
from .models import Reviews

class Form(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'stars']
