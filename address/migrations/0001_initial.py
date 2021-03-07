# Generated by Django 3.1.7 on 2021-03-07 11:09

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHname', models.CharField(max_length=50, verbose_name='Shop name')),
                ('SHgover', models.CharField(choices=[('ALEX', 'Alexandria'), ('ASW', 'Aswan'), ('ASYT', 'Asyut'), ('BEHA', 'Beheira'), ('BEF', 'Beni Suef'), ('CAI', 'Cairo'), ('DAKA', 'Dakahlia'), ('DAMA', 'Damietta'), ('FAI', 'Faiyum'), ('GHA', 'Gharbia'), ('GIZ', 'Giza'), ('ISM', 'Ismailia'), ('KAFH', 'Kafr El Sheikh'), ('LUX', 'Luxor'), ('MATH', 'Matruh'), ('MINA', 'Minya'), ('MONF', 'Monufia'), ('NEWY', 'New Valley'), ('NOSI', 'North Sinai'), ('POSA', 'Port Said'), ('QALA', 'Qalyubia'), ('QENA', 'Qena'), ('REDS', 'Red Sea'), ('SHAQ', 'Sharqia'), ('SOHG', 'Sohag'), ('SOSI', 'South Sinai'), ('SUZE', 'Suez')], max_length=50, verbose_name='Governorate')),
                ('SHaddress', models.TextField(max_length=300, verbose_name='Detailed address')),
                ('SHlocation', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Map location')),
                ('SHslug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
    ]
