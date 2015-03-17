# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150316_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='check_requested',
        ),
        migrations.AddField(
            model_name='customer',
            name='rating_requested',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
