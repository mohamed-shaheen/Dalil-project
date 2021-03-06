# Generated by Django 3.1.7 on 2021-04-22 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_product_prprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TYname', models.CharField(help_text="Ex: 'Market'or'Clinic'", max_length=50, verbose_name='Type name')),
                ('TYdesc', models.TextField(max_length=400, verbose_name='Description')),
                ('TYref_img', models.URLField(max_length=500, null=True, verbose_name='Link image')),
                ('TYslug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='CAdesc',
            field=models.TextField(max_length=400, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRprice',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', to='address.shop', verbose_name='Name of place'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='SHname',
            field=models.CharField(help_text='The name of your project, then choice type', max_length=50, verbose_name='Naming the place'),
        ),
    ]
