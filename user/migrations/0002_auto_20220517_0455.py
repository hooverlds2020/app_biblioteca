# Generated by Django 3.2 on 2022-05-17 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
