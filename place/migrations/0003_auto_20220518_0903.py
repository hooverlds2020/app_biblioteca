# Generated by Django 3.2 on 2022-05-18 14:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_alter_rack_uuid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campus',
            new_name='Sede',
        ),
        migrations.RenameField(
            model_name='rack',
            old_name='campus',
            new_name='sede',
        ),
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('5c3b5397-b359-4972-9352-a3c0f387250a')),
        ),
    ]
