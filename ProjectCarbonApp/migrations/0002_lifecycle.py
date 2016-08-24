# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lifecycle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, max_length=430)),
                ('category', models.CharField(null=True, max_length=430)),
                ('carbon_emission_factor', models.IntegerField(default=0, max_length=100000000)),
            ],
        ),
    ]
