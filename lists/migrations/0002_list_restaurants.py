# Generated by Django 2.2.5 on 2020-08-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='restaurants',
            field=models.ManyToManyField(blank=True, related_name='lists', to='restaurants.Restaurant'),
        ),
    ]
