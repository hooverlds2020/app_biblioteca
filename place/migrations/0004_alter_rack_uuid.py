# Generated by Django 3.2 on 2022-05-18 14:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_auto_20220518_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a5c6e786-de01-4c77-b7b9-f31dbd81f271')),
        ),
    ]
