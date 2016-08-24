# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0004_auto_20160812_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('purchase_unit', models.CharField(max_length=430, null=True)),
                ('purchase_unit_conversion_rate', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.AlterField(
            model_name='lifecycle',
            name='carbon_emission_factor',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='supplier_specifc',
            name='supplier_emission_factor',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='carbon_emission_factor',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
    ]
