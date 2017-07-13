import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.core.management.base import BaseCommand
from hitparade.models import Team, Official, Game, GameStat, GameBattingLineup

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

    #pprint.pprint(now.strftime("on %B %d, %Y"))
    #pprint.pprint(matchup)
    game = Game.objects.filter(
        season = now.year,
        on = now.strftime("on %B %d, %Y"),
        home_team = matchup["Home"],
        away_team = matchup["Away"])


def rotoWireGamesMatch(matchup1, matchup2):
    return matchup1['AwayTeam'] == matchup2["AwayTeam"] and matchup1['HomeTeam'] == matchup2["HomeTeam"]


def findLinkWithHref(html, hrefText):
    return html.findAll(href=hrefText)

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

def scrapeRotowire():
    r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')
    soup = BeautifulSoup(r.text, 'html.parser')
    now = datetime.now()
    complete = true;

    htmlMatches = [top.parent for top in soup.select("div.dlineups-topbox")]

    matchups = [createTeam(htmlMatch) for htmlMatch in htmlMatches]

    for matchup in matchups:
        if matchup["Official"]:
            complete = false #there should be a better way to check each needed item for completeness

        matchup["Away"] = GameStat.get_team_ref('code', matchup["AwayTeam"])[1]
        matchup["Home"] = GameStat.get_team_ref('code', matchup["HomeTeam"])[1]
        matchup["Official"] = GameStat.get_umpire_ref('name', matchup["Official"])[1]

        likeItems = [x for x in matchups if rotoWireGamesMatch(x, matchup)]

        matchupIndex = likeItems.index(matchup)

        matchup['Game'] = findGameFromRotoWire(matchup, now, matchupIndex)

        for person in matchup["AwayLineup"]:
            person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            gbl = GameBattingLineup.objects.create(game=matchup['Game'], 
                team=matchup['Away'], 
                player= person['Player'],
                position=person['Pos'],
                handedness=person['Handedness'],
                order=person['Order'])

            return

        for person in matchup["HomeLineup"]:
            person["Player"] = GameStat.get_player_ref('player', person["Name"])[1]

            gbl = GameBattingLineup.objects.create(game=matchup['Game'], 
                team=matchup['Home'], 
                player= person['Player'],
                position=person['Pos'],
                handedness=person['Handedness'],
                order=person['Order'])

    #pprint.pprint(matchups)
    return true

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def handle(self, *args, **options):
        errorText = ''
        start = datetime.now()
        wasScraped = false
        wasScrapeFull = false

        try:
            wasScraped = GameStat.wasRotowireLineupScraped(start)

            if !wasScraped:
                wasScrapeFull = scrapeRotowire()
                wasScraped = true;
        except:
            errorText = "Unexpected error:", sys.exc_info()[0]
            pprint.pprint(errorText)

        end = datetime.now()

        log = RotowireScrapeLineupLog.objects.create(
            started_at=start,
            ended_at=end,
            was_rotowire_scraped=wasScraped,
            was_data_complete=wasScrapeFull,
            error_text=errorText)

        