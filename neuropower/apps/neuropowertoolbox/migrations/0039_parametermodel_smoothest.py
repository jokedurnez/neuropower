# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-04 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuropowertoolbox', '0038_auto_20160309_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametermodel',
            name='SmoothEst',
            field=models.IntegerField(choices=[(1, 'Manual'), (2, 'Estimate')], default=1),
        ),
    ]
