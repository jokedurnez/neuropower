# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0006_designmodel_optimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='HardProb',
            field=models.BooleanField(default=True),
        ),
    ]
