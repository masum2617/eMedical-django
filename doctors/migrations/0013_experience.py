# Generated by Django 3.2.7 on 2021-10-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0012_auto_20211009_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50, null=True)),
                ('worked_from', models.DateField(null=True)),
                ('worked_to', models.DateField(null=True)),
                ('designation', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor')),
            ],
        ),
    ]
