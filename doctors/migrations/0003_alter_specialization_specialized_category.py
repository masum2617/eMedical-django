# Generated by Django 3.2.7 on 2021-10-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20211001_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialization',
            name='specialized_category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
