# Generated by Django 3.2.8 on 2021-11-12 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20211016_1858'),
        ('doctors', '0024_appointmenttime_from_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoint_date', models.CharField(max_length=50, null=True)),
                ('appoint_time', models.CharField(max_length=50, null=True)),
                ('appoint_day', models.CharField(max_length=50, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patient')),
            ],
        ),
    ]
