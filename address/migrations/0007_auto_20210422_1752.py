# Generated by Django 3.1.7 on 2021-04-22 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_auto_20210422_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AddField(
            model_name='shop',
            name='SHtype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='type_product', to='address.type', verbose_name='Place Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='type',
            name='TYname',
            field=models.CharField(help_text="Ex: 'Market'or'Clinic' etc..", max_length=50, verbose_name='Type name'),
        ),
    ]
