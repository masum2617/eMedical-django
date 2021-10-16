# Generated by Django 3.2.8 on 2021-10-16 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_auto_20211016_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.CharField(max_length=30, null=True)),
                ('appointment_date', models.CharField(max_length=30, null=True)),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.medicalhistory')),
            ],
        ),
    ]