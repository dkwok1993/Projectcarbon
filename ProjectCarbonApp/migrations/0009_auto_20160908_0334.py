# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0008_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='file_url',
        ),
        migrations.AddField(
            model_name='report',
            name='item',
            field=models.CharField(default=b'', max_length=430),
        ),
        migrations.AddField(
            model_name='report',
            name='purchase_unit',
            field=models.CharField(default=b'', max_length=430),
        ),
        migrations.AddField(
            model_name='report',
            name='unit',
            field=models.CharField(default=b'', max_length=430),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
