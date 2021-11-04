# Generated by Django 3.2.8 on 2021-11-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardiovascular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_category', models.CharField(max_length=100, null=True)),
                ('condition', models.CharField(max_length=100, null=True)),
                ('drug_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gastrointestinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_category', models.CharField(max_length=100, null=True)),
                ('condition', models.CharField(max_length=100, null=True)),
                ('drug_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respiratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_category', models.CharField(max_length=100, null=True)),
                ('condition', models.CharField(max_length=100, null=True)),
                ('drug_name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]