import requests
from flask_script import Command

from main import db
from Models import Team

class LoadTeams(Command):
    "Loads teams"

    def run(self):

        teams_url = "https://erikberg.com/mlb/teams.json"

        teams = requests.get(teams_url).json()

        for team in teams:

            t = Team.query.filter_by(abbreviation=team['abbreviation']).first()

            if not t:

                t = Team(
                    abbreviation=team['abbreviation'],
                    active=team['active'],
                    first_name=team['first_name'],
                    last_name=team['last_name'],
                    conference=team['conference'],
                    division=team['division'],
                    site_name=team['site_name'],
                    city=team['city'],
                    state=team['state'],
                    full_name=team['full_name'],
                )
                db.session.add(t)
                db.session.commit()

