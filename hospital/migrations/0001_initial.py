# Generated by Django 3.2.7 on 2021-10-02 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('doctors', '0006_alter_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50, null=True)),
                ('hospital_address', models.CharField(max_length=100, null=True)),
                ('hospital_country', models.CharField(max_length=50, null=True)),
                ('hospital_city', models.CharField(max_length=50, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(null=True)),
                ('appointment_status', models.BooleanField(default='inactive')),
                ('booking_date', models.DateField(null=True)),
                ('followup_date', models.DateField(null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patient')),
            ],
        ),
    ]
