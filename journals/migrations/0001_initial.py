# Generated by Django 4.0 on 2024-02-08 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20, verbose_name='Город')),
                ('img', models.ImageField(upload_to='image')),
                ('topic', models.CharField(max_length=50, verbose_name='Тема')),
                ('description', models.TextField(max_length=120, verbose_name='Описание')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 2, 8, 20, 22, 31, 381482))),
                ('reading_is', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='image')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journals.location')),
            ],
        ),
    ]
