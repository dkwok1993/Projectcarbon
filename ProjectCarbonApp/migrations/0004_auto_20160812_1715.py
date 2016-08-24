# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0003_supplierspecifc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier_specifc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=430)),
                ('supplier_emission_factor', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.DeleteModel(
            name='supplierspecifc',
        ),
        migrations.AlterField(
            model_name='lifecycle',
            name='carbon_emission_factor',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='carbon_emission_factor',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
