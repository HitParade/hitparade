import pprint
import datetime
import time

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Official, Venue, Game, get_games_to_update
from hitparade.utils import get_stattleship_client


class Command(BaseCommand):
    help = 'Updates game tables with data for games that have finished'


    def handle(self, *args, **options):

        print "Update Games!!!!1!"

        pp = pprint.PrettyPrinter(indent=2)

        s = get_stattleship_client()

        # Can't use this since the stattleship API refuses to return a single game by slug or ID or anything else.
        # games = get_games_to_update()

        # get last updated game
        g = Game.objects.filter(status=Game.STATUS_CLOSED).order_by('-started_at')[0]

        result = s.ss_get_results(sport='baseball',
                                league='mlb',
                                ep='games',
                                on=g.started_at.strftime("%Y-%m-%d")
                                # since=int(time.mktime(g.started_at.timetuple()))
                            )

        # Load conferences
        for o in result[0]['officials']:
            Official.create_from_ss(o)


        # Load Venues
        for v in result[0]['venues']:
            Venue.create_from_ss(v)


        # Load Games
        for g in result[0]['games']:
            Game.create_from_ss(g)
