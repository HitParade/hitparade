# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-10 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0003_auto_20170510_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='hit_location',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pitch',
            name='hit_type',
            field=models.CharField(max_length=2, null=True),
        ),
    ]