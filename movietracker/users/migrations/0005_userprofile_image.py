# Generated by Django 3.1.7 on 2021-12-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211216_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='deafult.jpg', upload_to='profile_pics'),
        ),
    ]
