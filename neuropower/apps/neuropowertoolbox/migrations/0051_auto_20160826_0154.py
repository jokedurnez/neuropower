# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-26 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuropowertoolbox', '0050_auto_20160825_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametermodel',
            name='maskfile',
            field=models.FileField(default='', upload_to='/Users/Joke/Documents/Onderzoek/ProjectsOngoing/Neuropower/neuropower-web/neuropower/media/maps'),
        ),
        migrations.AlterField(
            model_name='parametermodel',
            name='spmfile',
            field=models.FileField(default='', upload_to='/Users/Joke/Documents/Onderzoek/ProjectsOngoing/Neuropower/neuropower-web/neuropower/media/maps'),
        ),
    ]
