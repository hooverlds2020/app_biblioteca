# Generated by Django 3.2 on 2022-05-19 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0014_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4ee5da96-7548-4cfe-b92f-26940ebb6a20')),
        ),
    ]
