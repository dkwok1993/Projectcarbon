# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0007_auto_20160829_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=430)),
                ('file_url', models.CharField(max_length=256, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
