# Generated by Django 5.0.1 on 2024-02-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Назвние книги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото книги')),
                ('price', models.IntegerField(verbose_name='Прайс')),
                ('date_creating', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
