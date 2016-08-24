# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0005_auto_20160813_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lifecycle',
            name='category',
        ),
    ]
