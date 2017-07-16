import pprint

import requests
import sys
from bs4 import BeautifulSoup
from django.utils import timezone
from django.core.management.base import BaseCommand
from hitparade.models import Official, GameStat, RotowireScrapeOfficialLog

class Command(BaseCommand):
    help = 'Grabs ump stat data from Rotowire.'

    def createOfficial(self, htmlOfficial):
        tds = htmlOfficial.select('td')

        return {
            "Name":    tds[0].contents[1].strip(),
            "Game":    tds[1].contents[0].strip(),
            "Innings": tds[2].contents[0].strip(),
            "K":       tds[3].contents[0].strip(),
            "BB":      tds[4].contents[0].strip(),
            "K/9":     tds[5].contents[0].strip(),
            "BB/9":    tds[6].contents[0].strip(),
            "AVG":     tds[7].contents[0].strip(),
            "R":       tds[8].contents[0].strip(),
            "SLG":     tds[9].contents[0].strip(),
            "OBP":     tds[10].contents[0].strip(),
            "OPS":     tds[11].contents[0].strip(),
            "R/9":     tds[12].contents[0].strip()
        }

    def scrapeRotowire(self):
        r = requests.get('http://www.rotowire.com/daily/mlb/umpire_stats.php')

        soup = BeautifulSoup(r.text, 'html.parser')

        htmlOfficials = soup.select("#umpire tbody tr")

        officials = [self.createOfficial(htmlOfficial) for htmlOfficial in htmlOfficials]

        for official in officials:
            dbOff = GameStat.get_umpire_ref('name', official["Name"])[1]

            if dbOff is not None:
                dbOff.games = official["Game"]
                dbOff.innings = official["Innings"]
                dbOff.strike_outs = official["K"]
                dbOff.base_on_balls = official["BB"]
                dbOff.runs_scored = official["K/9"]
                dbOff.strikes_per_inning = official["BB/9"]
                dbOff.base_on_balls_per_inning = official["AVG"]
                dbOff.batting_average = official["R"]
                dbOff.slugging_average = official["SLG"]
                dbOff.runs = official["OBP"]
                dbOff.on_base_plus_slugging = official["OPS"]
                dbOff.on_base_percentage = official["R/9"]
        
        #pprint.pprint(officials)
        return True #don't know if this would ever be false


    def handle(self, *args, **options):
        errorText = ''
        start = timezone.now()
        wasScraped = False
        wasScrapeFull = False

        try:
            wasScraped = GameStat.wasRotowireOfficialScraped(start)

            if not wasScraped:
                wasScrapeFull = self.scrapeRotowire()
                wasScraped = True;
        except:
            errorText = "Unexpected error:", sys.exc_info()[0]
            pprint.pprint(sys.exc_info())

        end = timezone.now()

        log = RotowireScrapeOfficialLog.objects.create(
            started_at=start,
            ended_at=end,
            was_rotowire_scraped=wasScraped,
            was_data_complete=wasScrapeFull,
            error_text=errorText)