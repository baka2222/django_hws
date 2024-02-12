from django.db import models


'''СПАСИБО ЗА МЕСЯЦ:)'''
'''УДАЧИ ВО ФРОНТЕНДЕ'''


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Хэштеги категорий', default='#')

    def __str__(self):
        return self.name


class Cloth(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название одежды')
    description = models.TextField(max_length=250, blank=True, verbose_name='Описание')
    tags = models.ManyToManyField(Tag, verbose_name='Категория')

    def __str__(self):
        return self.title
