# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_trip_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
