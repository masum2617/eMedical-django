# Generated by Django 3.2.8 on 2021-10-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_patient_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
