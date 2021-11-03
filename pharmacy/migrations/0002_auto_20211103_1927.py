# Generated by Django 3.2.8 on 2021-11-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardiovascular',
            name='drug_image',
            field=models.ImageField(default='drug_default.jpg', upload_to='drugs/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='gastrointestinal',
            name='drug_image',
            field=models.ImageField(default='drug_default.jpg', upload_to='drugs/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='respiratory',
            name='drug_image',
            field=models.ImageField(default='drug_default.jpg', upload_to='drugs/%Y/%m/%d/'),
        ),
    ]
