# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-09 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models
import model_utils.fields


class Migration(migrations.Migration):

    replaces = [(b'hitparade', '0001_initial'), (b'hitparade', '0002_auto_20170503_2030'), (b'hitparade', '0003_auto_20170503_2039'), (b'hitparade', '0004_auto_20170503_2052'), (b'hitparade', '0005_auto_20170503_2054'), (b'hitparade', '0006_auto_20170503_2108'), (b'hitparade', '0007_auto_20170503_2109'), (b'hitparade', '0008_auto_20170504_0120'), (b'hitparade', '0009_auto_20170504_0121'), (b'hitparade', '0010_auto_20170504_1614'), (b'hitparade', '0011_auto_20170504_1614'), (b'hitparade', '0012_auto_20170504_1615'), (b'hitparade', '0013_auto_20170504_1617'), (b'hitparade', '0014_auto_20170504_1630'), (b'hitparade', '0015_auto_20170504_1917'), (b'hitparade', '0016_auto_20170509_1806')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=36)),
                ('conference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hitparade.Conference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('at_neutral_site', models.NullBooleanField()),
                ('attendance', models.IntegerField(blank=True, null=True)),
                ('away_team_outcome', models.CharField(max_length=16)),
                ('away_team_score', models.IntegerField(blank=True, null=True)),
                ('broadcast', models.CharField(max_length=32)),
                ('daytime', models.NullBooleanField()),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('ended_at', models.DateField(blank=True, null=True)),
                ('home_team_outcome', models.CharField(max_length=16)),
                ('home_team_score', models.IntegerField(blank=True, null=True)),
                ('humidity', models.CharField(max_length=32)),
                ('interval', models.CharField(max_length=32)),
                ('interval_number', models.IntegerField(blank=True, null=True)),
                ('interval_type', models.CharField(max_length=32)),
                ('label', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('on', models.CharField(max_length=64)),
                ('period', models.IntegerField(blank=True, null=True)),
                ('period_label', models.CharField(max_length=16)),
                ('score', models.CharField(max_length=16)),
                ('score_differential', models.IntegerField(blank=True, null=True)),
                ('scoreline', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('started_at', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=16)),
                ('internet_coverage', models.CharField(max_length=32)),
                ('satellite_coverage', models.CharField(max_length=32)),
                ('television_coverage', models.CharField(max_length=32)),
                ('temperature', models.CharField(max_length=8)),
                ('temperature_unit', models.CharField(max_length=8)),
                ('timestamp', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=64)),
                ('weather_conditions', models.CharField(max_length=64)),
                ('wind_direction', models.CharField(max_length=32)),
                ('wind_speed', models.IntegerField(blank=True, null=True)),
                ('wind_speed_unit', models.CharField(max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GameStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('game_date', models.DateField(blank=True, null=True)),
                ('local_game_time', models.DateField(blank=True, null=True)),
                ('ab', models.IntegerField(blank=True, null=True)),
                ('ba14', models.IntegerField(blank=True, null=True)),
                ('ba7', models.IntegerField(blank=True, null=True)),
                ('ba_curr_month', models.IntegerField(blank=True, null=True)),
                ('bb', models.IntegerField(blank=True, null=True)),
                ('car_ba', models.FloatField()),
                ('car_ba_bip', models.FloatField()),
                ('car_ba_curr_month', models.FloatField()),
                ('car_ba_for_half', models.FloatField()),
                ('car_ba_in_park', models.FloatField()),
                ('car_ba_off_pit', models.FloatField()),
                ('car_ba_vs_lhp', models.FloatField()),
                ('car_ba_vs_opp', models.FloatField()),
                ('car_ba_vs_rhp', models.FloatField()),
                ('car_ba_with_ump', models.FloatField()),
                ('car_era_with_ump', models.FloatField()),
                ('car_game_num', models.IntegerField(blank=True, null=True)),
                ('curr_hit_streak', models.IntegerField(blank=True, null=True)),
                ('doubles', models.IntegerField(blank=True, null=True)),
                ('gidp', models.IntegerField(blank=True, null=True)),
                ('game_num', models.IntegerField(blank=True, null=True)),
                ('h', models.IntegerField(blank=True, null=True)),
                ('hbp', models.IntegerField(blank=True, null=True)),
                ('hr', models.IntegerField(blank=True, null=True)),
                ('half', models.IntegerField(blank=True, null=True)),
                ('ibb', models.IntegerField(blank=True, null=True)),
                ('is_opp_pit_rhp', models.IntegerField(blank=True, null=True)),
                ('k', models.IntegerField(blank=True, null=True)),
                ('opp_bullpen_era', models.FloatField()),
                ('opp_pit_car_era', models.FloatField()),
                ('opp_pit_car_l', models.FloatField()),
                ('opp_pit_car_w', models.FloatField()),
                ('opp_pit_era', models.FloatField()),
                ('opp_pit_l', models.IntegerField(blank=True, null=True)),
                ('opp_pit_w', models.IntegerField(blank=True, null=True)),
                ('opp_score', models.IntegerField(blank=True, null=True)),
                ('pa', models.FloatField()),
                ('player_team_score', models.IntegerField(blank=True, null=True)),
                ('r', models.IntegerField(blank=True, null=True)),
                ('rbi', models.IntegerField(blank=True, null=True)),
                ('roe', models.IntegerField(blank=True, null=True)),
                ('sac', models.IntegerField(blank=True, null=True)),
                ('sb', models.IntegerField(blank=True, null=True)),
                ('sf', models.IntegerField(blank=True, null=True)),
                ('sea_ba', models.FloatField()),
                ('sea_ba_bip', models.FloatField()),
                ('sea_ba_for_half', models.FloatField()),
                ('sea_ba_in_park', models.FloatField()),
                ('sea_ba_vs_lhp', models.FloatField()),
                ('sea_ba_vs_opp', models.FloatField()),
                ('sea_ba_vs_rhp', models.FloatField()),
                ('sea_ba_with_ump', models.FloatField()),
                ('sea_era_with_ump', models.FloatField()),
                ('triples', models.IntegerField(blank=True, null=True)),
                ('was_start', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('uniform_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('slug', models.CharField(max_length=64)),
                ('active', models.NullBooleanField()),
                ('bats', models.CharField(max_length=12)),
                ('birth_date', models.DateField(null=True)),
                ('captain', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=128)),
                ('draft_overall_pick', models.IntegerField(blank=True, null=True)),
                ('draft_round', models.IntegerField(blank=True, null=True)),
                ('draft_season', models.IntegerField(blank=True, null=True)),
                ('draft_team_name', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=256)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('handedness', models.CharField(max_length=16)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('high_school', models.CharField(max_length=128)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('humanized_salary', models.CharField(max_length=16)),
                ('salary_currency', models.CharField(max_length=8)),
                ('mlbam_id', models.IntegerField(blank=True, null=True)),
                ('nickname', models.CharField(max_length=128)),
                ('position_abbreviation', models.CharField(max_length=8)),
                ('position_name', models.CharField(max_length=32)),
                ('pro_debut', models.DateField(blank=True, null=True)),
                ('school', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=32)),
                ('uniform_number', models.IntegerField(blank=True, null=True)),
                ('unit_of_height', models.CharField(max_length=16)),
                ('unit_of_weight', models.CharField(max_length=16)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('years_of_experience', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=7, unique=True)),
                ('location', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=64)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hitparade.Division')),
                ('colors', django_mysql.models.JSONField(default=list)),
                ('hashtags', django_mysql.models.JSONField(default=list)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ss_id', models.CharField(max_length=36, unique=True)),
                ('abbreviation', models.CharField(max_length=64)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=32, null=True)),
                ('field_type', models.CharField(max_length=16, null=True)),
                ('name', models.CharField(max_length=64, null=True)),
                ('slug', models.CharField(max_length=32, null=True)),
                ('state', models.CharField(max_length=2, null=True)),
                ('stadium_type', models.CharField(max_length=32, null=True)),
                ('time_zone', models.CharField(max_length=32, null=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='hp_ump',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_stat', to='hitparade.Official'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='opp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='opp_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hitparade.Player'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='opp_pit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hitparade.Player'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_stat', to='hitparade.Player'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='stadium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_stat', to='hitparade.Venue'),
        ),
        migrations.AddField(
            model_name='gamestat',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_stat', to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_game', to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_game', to='hitparade.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hitparade.Venue'),
        ),
        migrations.AddField(
            model_name='game',
            name='winning_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_game', to='hitparade.Team'),
        ),
        migrations.AlterField(
            model_name='player',
            name='captain',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='city',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='handedness',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='high_school',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='humanized_salary',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position_abbreviation',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position_name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='salary_currency',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='school',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='state',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='unit_of_height',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='unit_of_weight',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='draft_team_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='humidity',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='internet_coverage',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='interval',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='label',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='on',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='period_label',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='satellite_coverage',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='scoreline',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='television_coverage',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='temperature',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='temperature_unit',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='weather_conditions',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='wind_direction',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='wind_speed_unit',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
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
        migrations.AlterField(
            model_name='gamestat',
            name='local_game_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='gamestat',
            unique_together=set([('player', 'car_game_num')]),
        ),
    ]