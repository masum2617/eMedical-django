# Generated by Django 3.2.7 on 2021-10-09 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0013_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor'),
        ),
    ]