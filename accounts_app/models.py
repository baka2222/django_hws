from django.db import models
from django.contrib.auth.models import User

class AccountModel(User):
    GENDER = [
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ('Неопределенный', 'Неопределенный')
    ]

    EXPERIENCE = [
        ('Без опыта', 'Без опыта'),
        ('Менее года', 'Менее года'),
        ('Более года', 'Более года'),
        ('Больше 3 лет', 'Больше 3 лет')
    ]

    #Идей на 10 полей мало :/
    full_name = models.CharField(max_length=30, verbose_name='ФИО')
    nickname = models.CharField(max_length=20, verbose_name='Укажите свой ник', default='-')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    instagram = models.CharField(max_length=30, verbose_name='Инстаграм', blank=True)
    telegram = models.CharField(max_length=30, verbose_name='Тикток', blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Неопределенный')
    location = models.CharField(max_length=100, verbose_name='Место жительства')
    language_skills = models.TextField(verbose_name='Языки, которыми владеет пользователь', default='中文')
    experience = models.CharField(max_length=40, choices=EXPERIENCE, verbose_name='Опыт работы')
    bio = models.TextField(max_length=250, verbose_name='Чуть о себе')

    def __str__(self):
        return self.nickname





