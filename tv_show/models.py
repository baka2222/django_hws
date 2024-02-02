from django.db import models

class Movie(models.Model):
    GENRE = (
        ('Боевик', 'Боевик'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
        ('Триллеры', 'Триллеры')
    )
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(max_length=300, verbose_name='Опасние')
    image = models.ImageField(verbose_name='Изображение', upload_to='')
    actor = models.CharField(max_length=100, verbose_name='Актеры')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    trailer_url = models.URLField(verbose_name='Ссылка на трейлер')
    genre = models.CharField(choices=GENRE, max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    RATE_LIST = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ]

    film = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=300, verbose_name='Впечатления')
    stars = models.CharField(choices=RATE_LIST,
                             verbose_name='Оценка фильма',
                             max_length=40)
    def __str__(self):
        return self.movie