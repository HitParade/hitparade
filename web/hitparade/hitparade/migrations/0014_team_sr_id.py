# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-05 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0013_auto_20171004_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='sr_id',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
