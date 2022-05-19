# Generated by Django 3.2 on 2022-05-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=70)),
                ('description', models.TextField()),
            ],
        ),
    ]