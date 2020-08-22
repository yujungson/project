# Generated by Django 2.2.5 on 2020-08-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
