# Generated by Django 3.2 on 2022-05-19 02:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('abf23621-3640-4097-a311-2ad40809206f')),
        ),
    ]
