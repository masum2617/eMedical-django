# Generated by Django 3.2.7 on 2021-10-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='photos/doctors/'),
        ),
    ]
