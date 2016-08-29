# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCarbonApp', '0006_remove_lifecycle_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Supplier_specifc',
            new_name='Supplier_specific',
        ),
    ]
