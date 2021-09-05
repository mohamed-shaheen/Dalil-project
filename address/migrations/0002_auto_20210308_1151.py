# Generated by Django 3.1.7 on 2021-03-08 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CAname', models.CharField(max_length=50, verbose_name='Category name')),
                ('CAdesc', models.TextField(max_length=400, verbose_name='description')),
                ('CAref_img', models.URLField(max_length=400, null=True, verbose_name='Link image')),
                ('CAslug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='SHcreated_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='user_shop', to='auth.user', verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='SHcreated_dt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='SHnum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='shop',
            name='SHupdated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Updated by'),
        ),
        migrations.AddField(
            model_name='shop',
            name='SHupdated_dt',
            field=models.DateTimeField(null=True, verbose_name='Updated date'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRname', models.CharField(max_length=50, verbose_name='Product name')),
                ('PRdesc', models.TextField(help_text='Write about the product quality and how the product work ^_^ ..', max_length=400, verbose_name='description')),
                ('PRref', models.URLField(max_length=350, null=True, verbose_name='Outside reference link')),
                ('PRref_img', models.URLField(max_length=400, null=True, verbose_name='Link image')),
                ('PRslug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('PRcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='address.category', verbose_name='Category')),
                ('PRshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_product', to='address.shop', verbose_name='Shop name')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
