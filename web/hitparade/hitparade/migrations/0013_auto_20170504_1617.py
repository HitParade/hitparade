# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0012_auto_20170504_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
