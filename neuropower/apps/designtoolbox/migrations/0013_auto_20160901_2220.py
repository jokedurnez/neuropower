# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0012_auto_20160901_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='RestDur',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='designmodel',
            name='RestNum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
