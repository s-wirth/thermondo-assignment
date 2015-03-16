# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='check_requested',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='rating',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
