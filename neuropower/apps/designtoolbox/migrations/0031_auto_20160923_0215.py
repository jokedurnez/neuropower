# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-23 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0030_auto_20160922_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='conv_crit',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='designmodel',
            name='convergence',
            field=models.BooleanField(default=False),
        ),
    ]
