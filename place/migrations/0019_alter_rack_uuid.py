# Generated by Django 3.2 on 2022-05-19 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0018_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ea71baa8-2ac9-4f2c-9c3c-1b268e482c35')),
        ),
    ]
