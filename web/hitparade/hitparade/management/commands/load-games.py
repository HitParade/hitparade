import pprint
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Official, Venue, Game
from hitparade.utils import get_stattleship_client, move_ssid


class Command(BaseCommand):
    help = 'Parses application looking for mixpanel events.'


    def handle(self, *args, **options):

        print "Load Games!!!!1!"

        pp = pprint.PrettyPrinter(indent=2)

        s = get_stattleship_client()
        year = datetime.datetime.now().year
        season_slug = "mlb-%i" % year
        teams = Team.objects.all()

        for t in teams:

            page = 1
            len_games = -1

            while len_games != 0:

                result = s.ss_get_results(sport='baseball',
                                        league='mlb',
                                        ep='games',
                                        team_id=t.slug,
                                        page=page,
                                        per_page=40,
                                        season=season_slug
                                    )

                len_games = len(result[0]['games'])
                page = page + 1

                if len_games == 0:
                    continue


                # Load conferences
                for o in result[0]['officials']:
                    Official.create_from_ss(o)


                # Load Venues
                for v in result[0]['venues']:
                    Venue.create_from_ss(v)


                # Load Games
                for g in result[0]['games']:
                    g[u'season'] = year
                    Game.create_from_ss(g)

