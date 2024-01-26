# Generated by Django 5.0.1 on 2024-01-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300, verbose_name='Впечатления')),
                ('stars', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=40, verbose_name='Оценка фильма')),
            ],
        ),
    ]