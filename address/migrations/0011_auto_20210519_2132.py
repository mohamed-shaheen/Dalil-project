# Generated by Django 3.1.7 on 2021-05-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0010_product_prcreated_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRcreated_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
    ]
