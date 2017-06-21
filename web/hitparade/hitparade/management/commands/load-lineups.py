import pprint

import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand
from hitparade.models import Team, Official, Game, GameStat

def findNpop(data, select, contentIndex, arrayIndex = 0):
    item = data.select(select)

    return item[arrayIndex].contents[contentIndex].strip()

def findNpopTitle(data, select, contentIndex, arrayIndex = 0):
    item = data.select(select)

    return item[arrayIndex]['title']

def findlineup(htmlLineup, select):
    lineup = []

    for htmlPlayer in htmlLineup.select(select):
        lineup.append({
            "Pos": findNpop(htmlPlayer, '.dlineups-pos', 0),
            "Name": findNpopTitle(htmlPlayer, 'a', 0),
            "LR": findNpop(htmlPlayer, '.dlineups-lr', 0)
        })
    
    return lineup

def findLinkWithHref(html, hrefText):
    return html.findAll(href=hrefText)

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def createTeam(self, htmlMatch):
        ump =findLinkWithHref(htmlMatch, '/daily/mlb/umpire_stats.php')

        return {
            "AwayTeam": findNpop(htmlMatch, "div.dlineups-topboxleft", 0),
            "HomeTeam": findNpop(htmlMatch, "div.dlineups-topboxright", 2),
            "Time": findNpop(htmlMatch, "div.dlineups-topboxcenter-topline a", 0),
            "Weather": findNpop(htmlMatch, "div.dlineups-topboxcenter-bottomline", 0),
            "AwayPitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0),
            "HomePitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0, 1),
            "AwayLineup": findlineup(htmlMatch.select('.dlineups-half')[0], '.dlineups-vplayer'),
            "HomeLineup": findlineup(htmlMatch.select('.dlineups-half')[1], '.dlineups-hplayer'),
            "Ump": '' if not len(ump) else ump[0].text
        }

    def handle(self, *args, **options):
        r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')

        soup = BeautifulSoup(r.text, 'html.parser')

        htmlMatches = [top.parent for top in soup.select("div.dlineups-topbox")]

        matchups = [self.createTeam(htmlMatch) for htmlMatch in htmlMatches]

        #pprint.pprint(matchups)

        for matchup in matchups:
            matchup["Away"] = GameStat.get_team_ref('code', matchup["AwayTeam"])
            matchup["Home"] = GameStat.get_team_ref('code', matchup["HomeTeam"])
            matchup["OffKey"], matchup["Off"] = GameStat.get_umpire_ref('name', matchup["Ump"])

            for person in matchup["AwayLineup"]:
                person["Player"] = GameStat.get_player_ref('player', person["Name"])

            for person in matchup["HomeLineup"]:
                person["Player"] = GameStat.get_player_ref('player', person["Name"])

        pprint.pprint(matchups)