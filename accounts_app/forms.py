from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class AccountForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    nickname = forms.CharField(required=True)
    phone_number = forms.CharField(required=True,
                                   initial='+966',
                                   widget=forms.TextInput(attrs={'placeholder': "Введите номер телефона"}))
    instagram = forms.CharField(required=True,
                                initial='@',
                                widget=forms.TextInput(attrs={'placeholder': "Введите ник inst"}))
    telegram = forms.CharField(required=True,
                               initial='@',
                               widget=forms.TextInput(attrs={'placeholder': "Введите ник tg"}))
    gender = forms.ChoiceField(required=True, choices=models.AccountModel.GENDER)
    location = forms.CharField(required=True)
    language_skills = forms.CharField(required=True)
    experience = forms.ChoiceField(required=True, choices=models.AccountModel.EXPERIENCE)
    bio = forms.CharField(required=True, max_length=250)

    class Meta:
        model = models.AccountModel
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'full_name',
            'nickname',
            'phone_number',
            'instagram',
            'telegram',
            'gender',
            'location',
            'language_skills',
            'experience',
            'bio'
        ]

    def save(self, commit=True):
        user = super(AccountForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.full_name = self.cleaned_data['full_name']
        user.nickname = self.cleaned_data['nickname']
        user.phone_number = self.cleaned_data['phone_number']
        user.instagram = self.cleaned_data['instagram']
        user.telegram = self.cleaned_data['telegram']
        user.gender = self.cleaned_data['gender']
        user.location = self.cleaned_data['location']
        user.language_skills = self.cleaned_data['language_skills']
        user.experience = self.cleaned_data['experience']
        user.bio = self.cleaned_data['bio']

        if commit:
            user.save()
            return user



