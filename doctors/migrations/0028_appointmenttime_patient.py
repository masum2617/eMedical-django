# Generated by Django 3.2.8 on 2021-11-12 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20211016_1858'),
        ('doctors', '0027_auto_20211112_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmenttime',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patient'),
        ),
    ]
