# Generated by Django 3.2.8 on 2021-11-18 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0019_delete_patientappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor_sign',
            field=models.ImageField(default='default.png', upload_to='doctors/%Y/%m/%d/'),
        ),
    ]