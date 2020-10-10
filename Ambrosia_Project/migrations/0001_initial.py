# Generated by Django 3.1.1 on 2020-10-10 18:34

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_no', models.CharField(max_length=10)),
                ('epfNo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNo', models.CharField(max_length=20, unique=True)),
                ('Driverid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bill_No', models.CharField(max_length=10)),
                ('Description', models.TextField()),
                ('Service_Date', models.DateField(default=datetime.datetime.now)),
                ('Amount', models.FloatField()),
                ('VehicleNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Driving_Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('Start_Reading', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='Start date is invalid', message='Start reading must contain only numbers', regex='^[0-9]*$')])),
                ('End_Reading', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='End date is invalid', message='End reading must contain only numbers', regex='^[0-9]*$')])),
                ('Meter_Difference', models.IntegerField(blank=True)),
                ('VehicleNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.vehicle')),
            ],
        ),
    ]
