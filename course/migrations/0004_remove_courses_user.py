# Generated by Django 3.2.1 on 2021-05-09 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='user',
        ),
    ]
