# Generated by Django 3.2.7 on 2021-10-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='patients/%Y/%m/%d/'),
        ),
    ]
