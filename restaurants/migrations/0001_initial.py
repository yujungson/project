# Generated by Django 2.2.5 on 2020-09-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Accessibilities',
            },
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Atmosphere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Atmosphere',
            },
        ),
        migrations.CreateModel(
            name='Crowd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Crowds',
            },
        ),
        migrations.CreateModel(
            name='DiningOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'DiningOptions',
            },
        ),
        migrations.CreateModel(
            name='Highlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Highlights',
            },
        ),
        migrations.CreateModel(
            name='Offerings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Offerings',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='restaurant_photos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Planning',
            },
        ),
        migrations.CreateModel(
            name='ServiceOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Service Options',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=140)),
                ('guests', models.IntegerField(help_text='How many people will be staying?')),
                ('menu_1', models.CharField(max_length=150)),
                ('price_1', models.IntegerField()),
                ('menu_2', models.CharField(max_length=150)),
                ('price_2', models.IntegerField()),
                ('menu_3', models.CharField(max_length=150)),
                ('price_3', models.IntegerField()),
                ('menu_4', models.CharField(default=' ', max_length=150)),
                ('price_4', models.IntegerField()),
                ('menu_5', models.CharField(default=' ', max_length=150)),
                ('price_5', models.IntegerField()),
                ('accessibilities', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.Accessibility')),
                ('amenities', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.Amenities')),
                ('atmosphere', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.Atmosphere')),
                ('crowd', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.Crowd')),
                ('dining_options', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.DiningOptions')),
                ('highlights', models.ManyToManyField(blank=True, related_name='restaurants', to='restaurants.Highlights')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
