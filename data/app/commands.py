import requests

from flask_script import Command

from main import db
from utils import get_stattleship_client
from models import Conference, Division, Team, Player

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
