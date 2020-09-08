# Generated by Django 3.1.1 on 2020-09-07 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ambrosia_Project', '0005_accumulate_packet_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales_Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noOfPackets', models.IntegerField()),
                ('total_Price', models.FloatField()),
                ('cp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.categoryproduct')),
                ('product_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ambrosia_Project.packet_stock')),
            ],
        ),
    ]
