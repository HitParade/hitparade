# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-10 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0007_pitch_at_bat'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='at_bats_loaded',
            field=models.BooleanField(default=False),
        ),
    ]
