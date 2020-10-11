# Generated by Django 3.1.1 on 2020-10-10 13:08

import Ambrosia_Project.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nic', models.CharField(max_length=12, unique=True, validators=[Ambrosia_Project.validators.nic_validator])),
                ('epfNo', models.IntegerField(null=True, unique=True, validators=[django.core.validators.RegexValidator(code='EPF No is invalid', message='EPF No can only contain numbers', regex='^[0-9]*$')])),
                ('empImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('dob', models.DateField(null=True)),
                ('maritalStatus', models.CharField(choices=[('Married', 'Married'), ('UnMarried', 'Unmarried')], max_length=50)),
                ('contactNo', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='Invalid Contact No ', message='Contact No can only contain numbers', regex='^[0-9]*$'), django.core.validators.RegexValidator(code='Invalid Contact No ', message='Contact No length is invalid', regex='^.{10}$')])),
                ('doa', models.DateField(null=True)),
                ('basicSalary', models.FloatField(null=True)),
                ('empType', models.CharField(choices=[('Permanent', 'Permanent'), ('Temparory', 'Temparory')], max_length=50, null=True)),
                ('empGroup', models.CharField(choices=[('staff', 'Staff'), ('factory_Worker', 'FactoryWorker')], max_length=50, null=True)),
                ('designation', models.CharField(blank=True, choices=[('Factory_Officer', 'Factory_Officer'), ('AssistantFactory_Officer', 'AssistantFactory_Officer'), ('Clerk', 'Clerk'), ('Trainee', 'Trainee'), ('Supervisor', 'Supervisor'), ('Cashier', 'Cashier'), ('Driver', 'Driver')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('daytype', models.CharField(blank=True, choices=[('FD', 'FullDay'), ('HD', 'HalfDay')], max_length=20)),
                ('attendaceStatus', models.CharField(blank=True, choices=[('Pres', 'Present'), ('Abs', 'Absent')], max_length=50)),
                ('empID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='Ambrosia_Project.employee')),
            ],
            options={
                'unique_together': {('date', 'empID')},
            },
        ),
    ]
