# Generated by Django 3.1.1 on 2020-10-10 05:56

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
            name='BillItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.IntegerField(blank=True)),
                ('itemname', models.CharField(choices=[('BOPF', 'BOPF'), ('DUST 1', 'DUST 1'), ('DUST 2', 'DUST 2'), ('FGS', 'FGS')], max_length=10)),
                ('weight', models.CharField(choices=[('1Kg', ' 1Kg'), ('500g', '500g'), ('400g', '400g'), ('250g', '250Kg'), ('200g', '200g')], max_length=10)),
                ('itemPrice', models.FloatField(blank=True)),
                ('price', models.FloatField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Price_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BOPF', 'BOPF'), ('DUST 1', 'DUST 1'), ('DUST 2', 'DUST 2'), ('FGS', 'FGS')], max_length=10)),
                ('weight', models.CharField(choices=[('1Kg', ' 1Kg'), ('500g', '500g'), ('400g', '400g'), ('250g', '250Kg'), ('200g', '200g')], max_length=10)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(default=datetime.datetime.now)),
                ('total_Price', models.FloatField(blank=True)),
                ('invoice_id', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('available_stock', models.IntegerField()),
            ],
            options={
                'unique_together': {('category', 'weight')},
            },
        ),
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_name', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('category', 'weight')},
            },
        ),
        migrations.CreateModel(
            name='AddPackets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('noOfPackets', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('categoryProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.categoryproduct')),
            ],
        ),
    ]
