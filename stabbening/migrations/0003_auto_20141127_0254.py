# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stabbening', '0002_unit_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='orders',
            new_name='order',
        ),
    ]
