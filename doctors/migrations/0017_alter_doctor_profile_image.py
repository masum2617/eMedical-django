# Generated by Django 3.2.7 on 2021-10-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0016_alter_doctorspecialization_specialized_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='doctors/%Y/%m/%d/'),
        ),
    ]
