# Generated by Django 3.2.8 on 2021-11-18 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0020_prescription_doctor_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='doctor_sign',
        ),
    ]
