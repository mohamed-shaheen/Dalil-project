# Generated by Django 3.1.7 on 2021-03-17 21:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20210317_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='SHaddress',
            field=models.CharField(max_length=300, verbose_name='Detailed address'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='SHnum',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+201000000'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone number'),
        ),
    ]
