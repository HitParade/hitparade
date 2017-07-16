# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-16 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0014_auto_20170716_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='RotowireScrapeLineupLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('was_rotowire_scraped', models.BooleanField()),
                ('was_data_complete', models.BooleanField()),
                ('error_text', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RotowireScrapeOfficialLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('was_rotowire_scraped', models.BooleanField()),
                ('was_data_complete', models.BooleanField()),
                ('error_text', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
