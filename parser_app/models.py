from django.db import models

class Houses(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    location = models.TextField(max_length=300)
    img = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
