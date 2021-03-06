# Generated by Django 3.1.7 on 2021-12-19 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0003_movie_runtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('None', 'None'), ('Watching', 'Watching'), ('Plan to Watch', 'Plan To Watch'), ('Completed', 'Completed')], max_length=64, null=True)),
                ('favourite', models.BooleanField(default=False)),
                ('rating', models.FloatField(default=0.0)),
                ('movie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tracker.movie')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
