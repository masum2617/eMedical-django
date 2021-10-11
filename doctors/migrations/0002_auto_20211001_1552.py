# Generated by Django 3.2.7 on 2021-10-01 09:52

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialization',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='qualification',
            name='institution_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='qualification_degree',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='specialized_category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Medicine Specialists', 'Medicine Specialists'), ('Gastroenterologists', 'Gastroenterologists'), ('Neurologists', 'Neurologists')], max_length=142, null=True),
        ),
    ]