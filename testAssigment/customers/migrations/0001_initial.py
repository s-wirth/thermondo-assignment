# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('firstname', models.CharField(max_length=90)),
                ('lastname', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('check_requested', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
