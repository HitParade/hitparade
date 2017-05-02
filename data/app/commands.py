import os
import json
import datetime
import requests
import tempfile
import subprocess

from flask_script import Command

from main import app, db
from utils import *
from models import *

#TODO: Command to wrap all data loading commands

class LoadTeams(Command):
    "Loads teams"

    def run(self):

        s = get_stattleship_client()
        result = s.ss_get_results(sport='baseball',
                                league='mlb',
                                per_page=40
                                )

        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(result[0]['teams'])

        # Load conferences
        for c in result[0]['conferences']:
            if not Conference.query.filter_by(ss_id=c['id']).first():
                conf = Conference(
                        ss_id=c['id'],
                        name=c['name']
                    ).save()

        # Load divisions
        for d in result[0]['divisions']:
            if not Division.query.filter_by(ss_id=d['id']).first():

                conf = Conference.query.filter_by(ss_id=d['conference_id']).first()

                div = Division(
                        ss_id=d['id'],
                        name=d['name'],
                        conference_id=conf.id
                    ).save()

                conf.divisions.append(div)

        # Load teams
        for t in result[0]['teams']:
            if not Team.query.filter_by(ss_id=t['id']).first():

                div = Division.query.filter_by(ss_id=t['division_id']).first()

                team = Team(
                        ss_id=t['id'],
                        name=t['name'],
                        slug=t['slug'],
                        division_id=div.id,
                        location=t['location'],
                        nickname=t['nickname'],
                        colors=t['colors'],
                        hashtags=t['hashtags'],
                        latitude=t['latitude'],
                        longitude=t['longitude'],
                    ).save()


class LoadPlayers(Command):
    "Loads players"

    def run(self):

        s = get_stattleship_client()

        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        print "LoadPlayers"

        teams = Team.query.all()

        for t in teams:

            page = 1
            len_players = 1

            while len_players != 0:

                result = s.ss_get_results(sport='baseball',
                                        league='mlb',
                                        ep='players',
                                        team_id=t.slug,
                                        page=page,
                                        per_page=40,
                                        verbose=True,
                                        active=True
                                    )
                len_players = len(result[0]['players'])

                for player in result[0]['players']:
                    # pp.pprint(player)

                    if Player.query.filter_by(ss_id=player['id']).first():
                        continue

                    if not player['active']:
                        pass

                    p = Player(
                        team_id=t.id,
                        ss_id=player['id'],
                        slug=player['slug'],
                        active=player['active'],
                        bats=player['bats'],
                        birth_date=player['birth_date'],
                        captain=player['captain'],
                        city=player['city'],
                        draft_overall_pick=player['draft_overall_pick'],
                        draft_round=player['draft_round'],
                        draft_season=player['draft_season'],
                        draft_team_name=player['draft_team_name'],
                        name=player['name'],
                        first_name=player['first_name'],
                        last_name=player['last_name'],
                        handedness=player['handedness'],
                        height=player['height'],
                        high_school=player['high_school'],
                        salary=player['salary'],
                        humanized_salary=player['humanized_salary'],
                        salary_currency=player['salary_currency'],
                        mlbam_id=player['mlbam_id'],
                        nickname=player['nickname'],
                        position_abbreviation=player['position_abbreviation'],
                        position_name=player['position_name'],
                        pro_debut=player['pro_debut'],
                        school=player['school'],
                        state=player['state'],
                        uniform_number=player['uniform_number'] or None,
                        unit_of_height=player['unit_of_height'],
                        unit_of_weight=player['unit_of_weight'],
                        weight=player['weight'],
                        years_of_experience=player['years_of_experience'],
                    ).save()

                page = page + 1


class LoadGames(Command):
    """Load Games"""

    def run(self):

        year = datetime.datetime.now().year
        season_slug = "mlb-%i" % year

        s = get_stattleship_client()

        import pprint
        pp = pprint.PrettyPrinter(indent=2)

        print "LoadGames"

        teams = Team.query.all()

        for t in teams:
            print t

            page = 1
            len_games = -1

            while len_games != 0:

                result = s.ss_get_results(sport='baseball',
                                        league='mlb',
                                        ep='games',
                                        team_id=t.slug,
                                        page=page,
                                        per_page=40,
                                        season='mlb-2017'
                                    )

                len_games = len(result[0]['games'])
                page = page + 1

                if len_games == 0:
                    continue

                # Load conferences
                for o in result[0]['officials']:
                    if not Official.query.filter_by(ss_id=o['id']).first():
                        off = Official(
                                ss_id=o['id'],
                                name=o['name'],
                                first_name=o['first_name'],
                                last_name=o['last_name'],
                                uniform_number=o['uniform_number'] or 0,
                            ).save()

                # Load Venues
                for v in result[0]['venues']:
                    if not Venue.query.filter_by(ss_id=v['id']).first():
                        ven = Venue(
                                ss_id=v['id'],
                                name=v['name'],
                                abbreviation=v['abbreviation'],
                                capacity=v['capacity'],
                                city=v['city'],
                                field_type=v['field_type'],
                                slug=v['slug'],
                                state=v['state'],
                                stadium_type=v['stadium_type'],
                                time_zone=v['time_zone'],
                                longitude=v['longitude'],
                                latitude=v['latitude'],
                            ).save()

                # Load Venues
                for g in result[0]['games']:
                    if not Game.query.filter_by(ss_id=g['id']).first():

                        home_team_id = Team.query.filter_by(ss_id=g['home_team_id']).first().id
                        away_team_id = Team.query.filter_by(ss_id=g['away_team_id']).first().id
                        venue_id = Venue.query.filter_by(ss_id=g['venue_id']).first().id

                        winning_team_id = None
                        if g['winning_team_id']:
                            winning_team_id = Team.query.filter_by(ss_id=g['winning_team_id']).first().id

                        gam = Game(
                                ss_id=g['id'],
                                home_team_id=home_team_id,
                                away_team_id=away_team_id,
                                winning_team_id=winning_team_id,
                                venue_id=venue_id,
                                season=year,
                                at_neutral_site=g['at_neutral_site'],
                                attendance=g['attendance'],
                                away_team_outcome=g['away_team_outcome'],
                                away_team_score=g['away_team_score'],
                                broadcast=g['broadcast'],
                                daytime=g['daytime'],
                                duration=g['duration'],
                                ended_at=g['ended_at'],
                                home_team_outcome=g['home_team_outcome'],
                                home_team_score=g['home_team_score'],
                                humidity=g['humidity'],
                                interval=g['interval'],
                                interval_number=g['interval_number'],
                                interval_type=g['interval_type'],
                                label=g['label'],
                                name=g['name'],
                                on=g['on'],
                                period=g['period'],
                                period_label=g['period_label'],
                                score=g['score'],
                                score_differential=g['score_differential'],
                                scoreline=g['scoreline'],
                                slug=g['slug'],
                                started_at=g['started_at'],
                                status=g['status'],
                                internet_coverage=g['internet_coverage'],
                                satellite_coverage=g['satellite_coverage'],
                                television_coverage=g['television_coverage'],
                                temperature=g['temperature'],
                                temperature_unit=g['temperature_unit'],
                                timestamp=g['timestamp'],
                                title=g['title'],
                                weather_conditions=g['weather_conditions'],
                                wind_direction=g['wind_direction'],
                                wind_speed=g['wind_speed'],
                                wind_speed_unit=g['wind_speed_unit'],
                            ).save()


class UpdateGames(Command):
    """Update Games"""


    def run(self):
        print "Update Games"

        games_to_update = get_games_to_update()

        for game in games_to_update:
            print game


class LoadHistorical(Command):
    """Load Historical BIS Data"""


    def run(self):
        print "Load BIS Historical Data"

        import pprint
        pp = pprint.PrettyPrinter(indent=2)

        json_file = "/tmp/HistData2.json"

        if not os.path.isfile(json_file):

            f = tempfile.NamedTemporaryFile(delete=False)
            key = os.path.join(app.config['AWS_S3_BUCKET_BASE_KEY'], app.config['BIS_HISTORICAL_ZIP'])

            s3_get_file(app.config['AWS_S3_BUCKET_NAME'], key, f)

            p = subprocess.Popen(["unzip", "-o", f.name, "-d", os.path.dirname(f.name)], stdout=subprocess.PIPE)
            p.communicate()


        with open(json_file) as data_file:
            data = json.load(data_file)

        # pp.pprint(GameStat.key_map)

        for d in data:

            # Ignore Expos data, they're no longer a team
            if d['Team'] in GameStat.teams_ignored or \
                d['Opp'] in GameStat.teams_ignored:
                continue

            pp.pprint(d)

            kwargs = {}

            for bis_key, hp_key in GameStat.key_map.iteritems():

                if callable(hp_key):
                    k, v = hp_key(bis_key, d[bis_key])
                    kwargs[k] = v
                else:
                    kwargs[hp_key] = d[bis_key]

            pp.pprint(kwargs)

            GameStat(**kwargs).save()


