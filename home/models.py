from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назвние книги')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(verbose_name='Фото книги')
    price = models.IntegerField(verbose_name='Прайс')
    date_creating = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  #Не понял зачем
