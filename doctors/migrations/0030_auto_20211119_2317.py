# Generated by Django 3.2.8 on 2021-11-19 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0029_auto_20211112_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmenttime',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointmenttime',
            name='month',
        ),
    ]
