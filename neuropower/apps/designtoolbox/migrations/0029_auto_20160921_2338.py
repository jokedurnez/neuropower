# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-21 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0028_designmodel_shareid'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='taskID',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='designmodel',
            name='taskstatus',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
