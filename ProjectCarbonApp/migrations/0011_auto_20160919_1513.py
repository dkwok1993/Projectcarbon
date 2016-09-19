# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0010_auto_20160909_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.IntegerField()),
                ('name', models.CharField(max_length=430, null=True)),
                ('purchase_unit', models.CharField(max_length=430, null=True)),
                ('units', models.DecimalField(max_digits=12, decimal_places=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Upload',
        ),
    ]
