# Generated by Django 4.1 on 2022-08-15 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='room_name',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
