from django import forms
from .parser_funcs import *
from .models import Houses


class ParserForm(forms.Form):
    CHOISES = [
        ('house.kg', 'house.kg')
    ]
    media_type = forms.ChoiceField(choices=CHOISES)

    class Meta:
        fields = ['media_type']

    def parser(self):
        if self.data['media_type'] == 'house.kg':
            houses = parser()
            for i in houses:
                Houses.objects.create(**i)




