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
            print t

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

                    o = move_ssid(o)

                    o[u'uniform_number'] = o['uniform_number'] or 0

                    off, created = Official.objects.get_or_create(ss_id=o['ss_id'])
                    off.update(**o)
                    off.save()

                # Load Venues
                for v in result[0]['venues']:

                    v = move_ssid(v)

                    ven, created = Venue.objects.get_or_create(ss_id=v['ss_id'])
                    ven.update(**v)
                    ven.save()

                # Load Games
                for g in result[0]['games']:

                    g = move_ssid(g)

                    g[u'season'] = year
                    g[u'home_team'] = Team.objects.get(ss_id=g['home_team_id'])
                    g[u'away_team'] = Team.objects.get(ss_id=g['away_team_id'])
                    g[u'venue'] = Venue.objects.get(ss_id=g['venue_id'])

                    if g['winning_team_id']:
                        g['winning_team'] = Team.objects.get(ss_id=g['winning_team_id'])

                    del g['home_team_id']
                    del g['away_team_id']
                    del g['venue_id']
                    del g['winning_team_id']

                    pp.pprint(g)

                    gam, created = Game.objects.get_or_create(ss_id=g['ss_id'])
                    gam.update(**g)
                    gam.save()

