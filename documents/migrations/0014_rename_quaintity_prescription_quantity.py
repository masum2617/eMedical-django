# Generated by Django 3.2.8 on 2021-11-08 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0013_auto_20211108_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='quaintity',
            new_name='quantity',
        ),
    ]