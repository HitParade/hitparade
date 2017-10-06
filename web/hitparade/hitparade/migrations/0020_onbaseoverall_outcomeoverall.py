# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0019_outsoverall'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnBaseOverall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('s', models.IntegerField(null=True)),
                ('d', models.IntegerField(null=True)),
                ('t', models.IntegerField(null=True)),
                ('hr', models.IntegerField(null=True)),
                ('tb', models.IntegerField(null=True)),
                ('bb', models.IntegerField(null=True)),
                ('ibb', models.IntegerField(null=True)),
                ('hbp', models.IntegerField(null=True)),
                ('fc', models.IntegerField(null=True)),
                ('roe', models.IntegerField(null=True)),
                ('cycle', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutcomeOverall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('klook', models.IntegerField(null=True)),
                ('kswing', models.IntegerField(null=True)),
                ('ktotal', models.IntegerField(null=True)),
                ('ball', models.IntegerField(null=True)),
                ('iball', models.IntegerField(null=True)),
                ('dirtball', models.IntegerField(null=True)),
                ('foul', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]