# Generated by Django 4.0 on 2022-02-24 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
    ]
