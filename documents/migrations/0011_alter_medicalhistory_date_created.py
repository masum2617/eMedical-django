# Generated by Django 3.2.8 on 2021-10-16 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_medicalhistory_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
