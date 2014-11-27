# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stabbening', '0004_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='city',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
