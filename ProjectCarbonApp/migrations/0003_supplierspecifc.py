# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0002_lifecycle'),
    ]

    operations = [
        migrations.CreateModel(
            name='supplierspecifc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=430)),
                ('supplier_emission_factor', models.IntegerField(default=0, max_length=100000000)),
            ],
        ),
    ]
