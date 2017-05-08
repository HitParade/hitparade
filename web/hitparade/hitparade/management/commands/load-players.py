import pprint

from django.db import models
from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Player
from hitparade.utils import get_stattleship_client, move_ssid


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

                result = s.ss_get_results(sport='baseball',
                                        league='mlb',
                                        ep='players',
                                        team_id=t.slug,
                                        page=page,
                                        per_page=40,
                                        verbose=True,
                                        active=True
                                    )
                len_players = len(result[0]['players'])

                for p in result[0]['players']:

                    p = move_ssid(p)

                    p['team'] = t
                    p['uniform_number'] = p['uniform_number'] or 0
                    del p['team_id']
                    del p['league_id']

                    if not p['name'].strip():
                        p['name'] = "%s %s" % (p['first_name'], p['last_name'])

                    pp.pprint(p)

                    player, created = Player.objects.get_or_create(ss_id=p['ss_id'])
                    player.update(**p)
                    player.save()

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





