# Generated by Django 3.2 on 2022-05-19 19:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0012_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ad5a9857-5cd8-4530-a560-27e630cfcfb3')),
        ),
    ]