# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-05 19:29
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0002_auto_20160805_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='W',
            field=picklefield.fields.PickledObjectField(default='', editable=False),
        ),
    ]
