# Generated by Django 3.2.8 on 2021-10-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20211015_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='is_processing',
            field=models.BooleanField(default=False),
        ),
    ]
