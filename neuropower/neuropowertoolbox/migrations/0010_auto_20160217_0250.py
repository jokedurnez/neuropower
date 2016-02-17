# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuropowertoolbox', '0009_auto_20160217_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametermodel',
            name='ExcUnits',
            field=models.CharField(choices=[('p', 'units = p-values (SPM default)'), ('t', 'units = t-values (FSL default)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='parametermodel',
            name='Samples',
            field=models.IntegerField(choices=[(1, 'One-sample'), (2, 'Two-sample')]),
        ),
        migrations.AlterField(
            model_name='parametermodel',
            name='ZorT',
            field=models.CharField(choices=[('Z', 'Z'), ('T', 'T')], max_length=10),
        ),
    ]
