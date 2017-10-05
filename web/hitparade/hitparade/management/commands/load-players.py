import pprint

from django.db import models
from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Player
from hitparade.utils import get_stattleship_client, move_ssid, get_redis, get_redis_object, set_redis_object
redis_connection = get_redis()

class Command(BaseCommand):
    help = 'Parses application looking for mixpanel events.'


    def handle(self, *args, **options):

        print "Load Players!!!!1!"

        self.import_data()

        self.clean_dupes()


    def import_data(self):

        s = get_stattleship_client()

        import pprint
        pp = pprint.PrettyPrinter(indent=2)

        teams = Team.objects.all()

        for t in teams:

            page = 1
            len_players = 1

            while len_players != 0:
                key_ = t.slug + str(page) + str(40) + 'players'
                result = get_redis_object(redis_connection, key_)
                if result is None:
                    result = s.ss_get_results(sport='baseball',
                                              league='mlb',
                                              ep='players',
                                              team_id=t.slug,
                                              page=page,
                                              per_page=40,
                                              verbose=True,
                                              active=True
                                              )
                    set_redis_object(redis_connection, key_, result)
                len_players = len(result[0]['players'])


                for p in result[0]['players']:
                    p['team'] = t
                    Player.create_from_ss(p)


                page = page + 1


    def clean_dupes(self):

        import pprint
        pp = pprint.PrettyPrinter(indent=2)

        dupes = Player.objects.values('name').annotate(cnt=models.Count('id')).filter(cnt__gt=1).order_by('name')

        for d in dupes:
            print "**************************************"

            dupe_players = Player.objects.filter(name=d['name'])
            candidate = None

            for dp in dupe_players:

                # More than 2 dashes indicate a malformed slug
                # if dp.slug.count("-") > 2:
                #     continue

                if dp.slug.startswith("mlb-") or dp.mlbam_id is not None:
                    candidate = dp

            if not candidate:
                continue

            for dp in dupe_players:
                if dp != candidate:
                    dp.delete()





