# Generated by Django 4.1.7 on 2023-03-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcrud',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='postcrud',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
