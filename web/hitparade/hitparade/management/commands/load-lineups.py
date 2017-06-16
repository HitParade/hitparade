import pprint

import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

def findNpop(match, data, prop, select, contentIndex, arrayIndex = 0):
    item = data.select(select)
    match[prop] = item[arrayIndex].contents[contentIndex].strip()

def findlineup(htmlLineup, select):
    lineup = []

    for htmlPlayer in htmlLineup.select(select):
        player = {}

        findNpop(player, htmlPlayer, "Pos", '.dlineups-pos', 0)
        findNpop(player, htmlPlayer, "Name", 'a', 0)
        findNpop(player, htmlPlayer, "LR", '.dlineups-lr', 0)

        lineup.append(player)
    
    return lineup

class Command(BaseCommand):
    help = 'Grabs lineup data from Rotowire.'

    def handle(self, *args, **options):

        r = requests.get('http://www.rotowire.com/baseball/daily_lineups.htm')

        soup = BeautifulSoup(r.text, 'html.parser')

        htmlTops = soup.select("div.dlineups-topbox")

        htmlMatches = []

        for top in htmlTops:
            htmlMatches.append(top.parent)

        count = len(htmlMatches)

        matchups = []

        for htmlMatch in htmlMatches:
            match = {}

            findNpop(match, htmlMatch, "AwayTeam", "div.dlineups-topboxleft", 0)
            findNpop(match, htmlMatch, "HomeTeam", "div.dlineups-topboxright", 2)
            findNpop(match, htmlMatch, "Time", "div.dlineups-topboxcenter-topline a", 0)
            findNpop(match, htmlMatch, "Weather", "div.dlineups-topboxcenter-bottomline", 0)
            findNpop(match, htmlMatch, "AwayPitcher", "div.dlineups-pitchers a", 0)
            findNpop(match, htmlMatch, "HomePitcher", "div.dlineups-pitchers a", 0, 1)

            match["AwayLineup"] = findlineup(htmlMatch.select('.dlineups-half')[0], '.dlineups-vplayer')
            match["HomeLineup"] = findlineup(htmlMatch.select('.dlineups-half')[1], '.dlineups-hplayer')

            matchups.append(match)

        for item in matchups:
            pprint.pprint(item)