from django import forms
from .models import Review, Movie

class Form(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'stars', 'film']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description',
                  'image', 'actor',
                  'director', 'trailer_url',
                  'genre']
