# Generated by Django 3.1.7 on 2021-12-29 19:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_movie_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviestatus',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
