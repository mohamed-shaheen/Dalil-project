# Generated by Django 3.1.7 on 2021-03-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20210317_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRprice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
