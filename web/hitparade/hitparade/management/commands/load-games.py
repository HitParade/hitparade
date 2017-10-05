import pprint
import datetime
import time

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Official, Venue, Game
from hitparade.utils import get_stattleship_client, move_ssid, get_venues, get_key_or_null,get_redis, get_redis_object, set_redis_object
redis_connection = get_redis()

class Command(BaseCommand):
    help = 'Parses application looking for mixpanel events.'


    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--only-recent',
            action='store_true',
            dest='only_recent',
            default=False,
            help='Only update recent games, from the last closed game.',
        )


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

                kwargs = {
                    'sport': 'baseball',
                    'league': 'mlb',
                    'ep': 'games',
                    'team_id': t.slug,
                    'page': page,
                    'season': season_slug,
                    'per_page': 40,
                }

                if options['only_recent']:
                    started = Game.objects.filter(status=Game.STATUS_CLOSED).order_by('-started_at')[0].started_at
                    kwargs['since'] = int(time.mktime(started.timetuple()))
                    kwargs['status'] = Game.STATUS_CLOSED
                key_ = t.slug + str(page) + str(40) + str(season_slug) + 'games'
                result = get_redis_object(redis_connection, key_)
                if result is None:
                    result = s.ss_get_results(**kwargs)
                    set_redis_object(redis_connection, key_, result)
                if 'games' not in result[0]:
                    len_games = 0
                else:
                    len_games = len(result[0]['games'])

                page = page + 1

                if len_games == 0:
                    continue


                # Load conferences
                for o in result[0]['officials']:
                    Official.create_from_ss(o)

                venues, _, _  = get_venues()
                venue_cities = {}
                venue_names = {}
                for v in venues:
                    city_ = get_key_or_null(v,  'city')
                    venue_cities[city_] = v
                    venue_cities[city_.lower()] = v
                    name_ = get_key_or_null(v,  'name')
                    venue_names[name_] = v
                    venue_names[name_.lower()] = v

                pp.pprint(venues)
                pp.pprint(venue_cities)
                pp.pprint(venue_names)
                # Load Venues
                for v in result[0]['venues']:
                    sports_radar_venue = get_key_or_null(venue_names,  get_key_or_null(v, 'name') )
                    if sports_radar_venue is None:
                        sports_radar_venue = get_key_or_null(venue_cities,  get_key_or_null(v, 'city') )
                    if not sports_radar_venue is None and not type(sports_radar_venue) == type('s '):
                        v['distances_lf'] = get_key_or_null(sports_radar_venue,  'distances_lf')
                        v['distances_lcf'] = get_key_or_null(sports_radar_venue ,  'distances_lcf')
                        v['distances_cf'] = get_key_or_null(sports_radar_venue ,  'distances_cf')
                        v['distances_rcf'] = get_key_or_null(sports_radar_venue ,  'distances_rcf')
                        v['distances_rf'] = get_key_or_null(sports_radar_venue ,  'distances_rf')
                        v['distances_mlf'] = get_key_or_null(sports_radar_venue ,  'distances_mlf')
                        v['distances_mlcf'] = get_key_or_null(sports_radar_venue ,  'distances_mlcf')
                        v['distances_mrcf'] = get_key_or_null(sports_radar_venue ,  'distances_mrcf')
                        v['distances_mrf'] = get_key_or_null(sports_radar_venue ,  'distances_mrf')
                        v['sr_id'] = get_key_or_null(sports_radar_venue,  'id')
                        print("Found sports radar venue " + str(get_key_or_null(sports_radar_venue,  'name')))
                    else:
                        print(' sports radar venue is none or type string ' + str(sports_radar_venue))
                    Venue.create_from_ss(v)


                # Load Games
                for g in result[0]['games']:
                    g[u'season'] = year
                    try:
                        Game.create_from_ss(g)
                    except:
                        print("Error creating game")
                        print(g)

