# Generated by Django 3.1 on 2020-09-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ambrosia_Project', '0002_funds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowance_by_price', models.FloatField()),
                ('incentive_1', models.FloatField()),
                ('incentive_2', models.FloatField()),
            ],
            options={
                'db_table': 'allowance',
            },
        ),
    ]