import pprint
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import *
from hitparade.utils import get_stattleship_client, move_ssid


class Command(BaseCommand):
    help = 'Load At-Bats from Stattleship.'


    def handle(self, *args, **options):

        print "Load At Bats!!!!1!"

        pp = pprint.PrettyPrinter(indent=2)

        s = get_stattleship_client()
        year = datetime.datetime.now().year
        season_slug = "mlb-%i" % year
        games = Game.objects.filter(status=Game.STATUS_CLOSED)

        for game in games:
            print game

            page = 1
            len_atbats = -1

            while len_atbats != 0:

                result = s.ss_get_results(sport='baseball',
                                        league='mlb',
                                        ep='at_bats',
                                        game_id=game.ss_id,
                                        page=page,
                                        per_page=40
                                    )

                print result[0].keys()

                pp.pprint(result[0]['at_bats'][0])

                len_atbats = len(result[0]['at_bats'])
                page = page + 1


                if len_atbats == 0:
                    continue


                # # Load Officials
                # for o in result[0]['officials']:
                #     Official.create_from_ss(o)


                # # Load Venues
                # for v in result[0]['venues']:
                #     Venue.create_from_ss(v)


                # # Load Games
                # for g in result[0]['games']:
                #     g[u'season'] = year
                #     Game.create_from_ss(g)


                # Load Players
                for p in result[0]['hitters']:
                    Player.create_from_ss(p)


                for p in result[0]['pitchers']:
                    Player.create_from_ss(p)


                # Load pitches
                for p in result[0]['baseball_pitches']:

                    pp.pprint(p)

                    p['game'] = game
                    Pitch.create_from_ss(p)


                return

