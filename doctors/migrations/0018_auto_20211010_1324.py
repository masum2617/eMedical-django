# Generated by Django 3.2.7 on 2021-10-10 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0017_alter_doctor_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(default='img/default.png', upload_to='doctors/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='doctorspecialization',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor'),
        ),
    ]