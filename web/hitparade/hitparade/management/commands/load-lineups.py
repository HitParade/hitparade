import pprint

import requests
import sys
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand
from hitparade.models import Team, Official, Game, GameStat, GameBattingLineup, RotowireScrapeLineupLog

def findNpop(data, select, contentIndex, arrayIndex = 0):
    item = data.select(select)

    return item[arrayIndex].contents[contentIndex].strip()

def findNpopTitle(data, select, arrayIndex = 0):
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
    games = Game.objects.filter(
        season = now.year,
        on = now.strftime("on %B %d, %Y"),
        home_team = matchup["Home"],
        away_team = matchup["Away"])

    return games[index]


def rotoWireGamesMatch(matchup1, matchup2):
    return matchup1['AwayTeam'] == matchup2["AwayTeam"] and matchup1['HomeTeam'] == matchup2["HomeTeam"]


def findLinkWithHref(html, hrefText):
    return html.findAll(href=hrefText)

def createTeam(htmlMatch):
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

def scrapeRotowire():
    r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')
    soup = BeautifulSoup(r.text, 'html.parser')
    now = datetime.now()
    complete = True;

    htmlMatches = [top.parent for top in soup.select("div.dlineups-topbox")]

    matchups = [createTeam(htmlMatch) for htmlMatch in htmlMatches]

    for matchup in matchups:
        comeplete = (matchup["Official"]
            and matchup["HomePitcher"]
            and matchup["AwayPitcher"]
            and matchup["AwayLineup"]
            and matchup["HomeLineup"])

        matchup["Away"] = GameStat.get_team_ref('code', matchup["AwayTeam"])[1]
        matchup["Home"] = GameStat.get_team_ref('code', matchup["HomeTeam"])[1]
        matchup["StartingOfficial"] = GameStat.get_umpire_ref('name', matchup["Official"])[1]
        matchup["StartingHomePitcher"] = GameStat.get_player_ref('player', matchup["HomePitcher"])[1]
        matchup["StartingAwayPitcher"] = GameStat.get_player_ref('player', matchup["AwayPitcher"])[1]

        likeItems = [x for x in matchups if rotoWireGamesMatch(x, matchup)]

        matchupIndex = likeItems.index(matchup)

        matchup['Game'] = findGameFromRotoWire(matchup, now, matchupIndex)

        if (matchup['Game'].official is None
            and matchup['StartingOfficial']):
            matchup['Game'].official = matchup['StartingOfficial']

        if (not matchup['Game'].starting_home_pitcher 
            and matchup['StartingHomePitcher']):
            matchup['Game'].starting_home_pitcher = matchup['StartingHomePitcher']

        if (not matchup['Game'].starting_away_pitcher 
            and matchup['StartingAwayPitcher']):
            matchup['Game'].starting_away_pitcher = matchup['StartingAwayPitcher']

        for person in matchup["AwayLineup"]:
            person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            gbl = GameBattingLineup.objects.get_or_create(game=matchup['Game'], 
                team=matchup['Away'], 
                player= person['Player'],
                position=person['Pos'],
                handedness=person['Handedness'],
                order=person['Order'])

        for person in matchup["HomeLineup"]:
            person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            gbl = GameBattingLineup.objects.get_or_create(game=matchup['Game'], 
                team=matchup['Home'], 
                player= person['Player'],
                position=person['Pos'],
                handedness=person['Handedness'],
                order=person['Order'])
    return True

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def handle(self, *args, **options):
        errorText = ''
        start = timezone.now()
        wasScraped = False
        wasScrapeFull = False

        try:
            wasScraped = GameStat.wasRotowireLineupScraped(start)

            if not wasScraped:
                wasScrapeFull = scrapeRotowire()
                wasScraped = True;
        except:
            errorText = "Unexpected error:", sys.exc_info()[0]
            pprint.pprint(sys.exc_info())

        end = timezone.now()

        log = RotowireScrapeLineupLog.objects.create(
            started_at=start,
            ended_at=end,
            was_rotowire_scraped=wasScraped,
            was_data_complete=wasScrapeFull,
            error_text=errorText)

        