# Generated by Django 2.2.5 on 2020-09-04 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='superhost',
        ),
    ]
