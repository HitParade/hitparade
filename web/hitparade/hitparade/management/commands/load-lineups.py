import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime
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

    for index, item in enumerate(htmlLineup.select(select)):
        lineup.append({
            "Pos": findNpop(item, '.dlineups-pos', 0),
            "Name": findNpopTitle(item, 'a', 0),
            "Handedness": findNpop(item, '.dlineups-lr', 0),
            "Order": index
        })
    
    return lineup

def findGameFromRotoWire(matchup, now, index):
    game = Game.objects.filter(
        season = now.year,
        on = now.strftime("on %B %d, %Y"),
        home_team = matchup["Home"],
        away_team = matchup["Away"])

    return game[index]

def rotoWireGamesMatch(matchup1, matchup2):
    return matchup1['AwayTeam'] == matchup2["AwayTeam"] and matchup1['HomeTeam'] == matchup2["HomeTeam"]


def findLinkWithHref(html, hrefText):
    return html.findAll(href=hrefText)

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def createTeam(self, htmlMatch):
        ump = findLinkWithHref(htmlMatch, '/daily/mlb/umpire_stats.php')

        return {
            "AwayTeam": findNpop(htmlMatch, "div.dlineups-topboxleft", 0),
            "HomeTeam": findNpop(htmlMatch, "div.dlineups-topboxright", 2),
            "Time": findNpop(htmlMatch, "div.dlineups-topboxcenter-topline a", 0),
            "Weather": findNpop(htmlMatch, "div.dlineups-topboxcenter-bottomline", 0),
            "AwayPitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0),
            "HomePitcher": findNpop(htmlMatch, "div.dlineups-pitchers a", 0, 1),
            "AwayLineup": findlineup(htmlMatch.select('.dlineups-half')[0], '.dlineups-vplayer'),
            "HomeLineup": findlineup(htmlMatch.select('.dlineups-half')[1], '.dlineups-hplayer'),
            "Official": None if not len(ump) else ump[0].text
        }

    def handle(self, *args, **options):
        r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')

        soup = BeautifulSoup(r.text, 'html.parser')
        now = datetime.now()

        htmlMatches = [top.parent for top in soup.select("div.dlineups-topbox")]

        matchups = [self.createTeam(htmlMatch) for htmlMatch in htmlMatches]

        for matchup in matchups:
            matchup["Away"] = GameStat.get_team_ref('code', matchup["AwayTeam"])[1]
            matchup["Home"] = GameStat.get_team_ref('code', matchup["HomeTeam"])[1]
            matchup["Official"] = GameStat.get_umpire_ref('name', matchup["Official"])[1]

            likeItems = [x for x in matchups if rotoWireGamesMatch(x, matchup)]
            matchupIndex = likeItems.index(matchup)

            for person in matchup["AwayLineup"]:
                person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            for person in matchup["HomeLineup"]:
                person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            matchup['Game'] = findGameFromRotoWire(matchup, now, matchupIndex)
        
        #pprint.pprint(matchups)