# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hitparade', '0013_auto_20170504_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestat',
            name='ab',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='ba14',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='ba7',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='ba_curr_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='bb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_bip',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_curr_month',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_for_half',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_in_park',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_off_pit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_vs_lhp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_vs_opp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_vs_rhp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_ba_with_ump',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_era_with_ump',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='car_game_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='curr_hit_streak',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='doubles',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='game_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='game_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='gidp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='h',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='half',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='hbp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='hr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='ibb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='is_opp_pit_rhp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='k',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='local_game_time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_bullpen_era',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_car_era',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_car_l',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_car_w',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_era',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_l',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_pit_w',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='opp_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='pa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='player_team_score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='r',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='rbi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='roe',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sac',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_bip',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_for_half',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_in_park',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_vs_lhp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_vs_opp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_vs_rhp',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_ba_with_ump',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sea_era_with_ump',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='sf',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='triples',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamestat',
            name='was_start',
            field=models.IntegerField(null=True),
        ),
    ]