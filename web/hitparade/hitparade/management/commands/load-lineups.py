import pprint

import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

def findNpop(data, select, contentIndex, arrayIndex = 0):
    item = data.select(select)

    return item[arrayIndex].contents[contentIndex].strip()

def findlineup(htmlLineup, select):
    lineup = []

    for htmlPlayer in htmlLineup.select(select):
        lineup.append({
            "Pos": findNpop(htmlPlayer, '.dlineups-pos', 0),
            "Name": findNpop(htmlPlayer, 'a', 0),
            "LR": findNpop(htmlPlayer, '.dlineups-lr', 0)
        })
    
    return lineup

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def createTeam(self, htmlMatch):
        return {
            "AwayTeam": findNpop(htmlMatch, "div.dlineups-topboxleft", 0),
            "HomeTeam": findNpop(htmlMatch, "div.dlineups-topboxright", 2),
            "Time": findNpop(htmlMatch, "div.dlineups-topboxcenter-topline a", 0),
            "Weather": findNpop(htmlMatch, "div.dlineups-topboxcenter-bottomline", 0),
            "AwayPitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0),
            "HomePitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0, 1),
            "AwayLineup": findlineup(htmlMatch.select('.dlineups-half')[0], '.dlineups-vplayer'),
            "HomeLineup": findlineup(htmlMatch.select('.dlineups-half')[1], '.dlineups-hplayer')
        }

    def handle(self, *args, **options):
        r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')

        soup = BeautifulSoup(r.text, 'html.parser')

        htmlMatches = [top.parent for top in soup.select("div.dlineups-topbox")]

        matchups = [self.createTeam(htmlMatch) for htmlMatch in htmlMatches]

        pprint.pprint(matchups)