# Generated by Django 3.2.8 on 2021-10-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0020_alter_doctor_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='doctors/%Y/%m/%d/'),
        ),
    ]
