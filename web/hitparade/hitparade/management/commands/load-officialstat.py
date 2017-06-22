import pprint

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from hitparade.models import Official, GameStat

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

    def handle(self, *args, **options):
        r = requests.get('http://www.rotowire.com/daily/mlb/umpire_stats.php')

        soup = BeautifulSoup(r.text, 'html.parser')

        htmlOfficials = soup.select("#umpire tbody tr")

        officials = [self.createOfficial(htmlOfficial) for htmlOfficial in htmlOfficials]

        for official in officials:
            official["Official"] = GameStat.get_umpire_ref('name', official["Name"])[1]
        
        pprint.pprint(officials)