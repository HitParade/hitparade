# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0010_auto_20170504_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hitparade.Venue'),
        ),
    ]
