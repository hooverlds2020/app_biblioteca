# Generated by Django 3.2 on 2022-05-18 15:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_alter_rack_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('fb3e311e-875a-4d1f-9dc5-719461142ac1')),
        ),
    ]
