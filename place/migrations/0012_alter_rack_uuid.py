# Generated by Django 3.2 on 2022-05-19 14:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('a0c018b7-de5b-4990-b0b5-df0c478373a6')),
        ),
    ]