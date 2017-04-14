import requests

from flask_script import Command

from main import db
from utils import get_stattleship_client
from models import Conference, Division, Team

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

        print "LoadPlayers"

        s = get_stattleship_client()
        result = s.ss_get_results(sport='baseball',
                                league='mlb',
                                per_page=1
                                )

        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(result[0])
