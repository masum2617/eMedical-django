# Generated by Django 3.2.7 on 2021-10-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_medicalhistory_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
