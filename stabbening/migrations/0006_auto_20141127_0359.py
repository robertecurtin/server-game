# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stabbening', '0005_unit_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='owner',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='owner',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
    ]
