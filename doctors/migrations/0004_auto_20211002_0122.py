# Generated by Django 3.2.7 on 2021-10-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_specialization_specialized_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorspecialization',
            name='doctor_specialization',
        ),
        migrations.AddField(
            model_name='doctorspecialization',
            name='specialized_category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Specialization',
        ),
    ]
