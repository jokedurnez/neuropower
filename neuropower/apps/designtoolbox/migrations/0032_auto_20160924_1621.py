# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0031_auto_20160923_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='email',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='designmodel',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]