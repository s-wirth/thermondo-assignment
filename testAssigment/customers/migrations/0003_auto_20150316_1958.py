# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150316_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='check_requested',
            field=models.IntegerField(verbose_name=0, default='0'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=90, default='Not registered'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(max_length=90, default='Unknown'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='rating',
            field=models.IntegerField(default='-1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(max_length=90, default='Unknown'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.IntegerField(primary_key=True, default='0', serialize=False),
            preserve_default=True,
        ),
    ]
