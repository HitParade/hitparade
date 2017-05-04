import pprint

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Player
from hitparade.utils import get_stattleship_client, move_ssid


class Command(BaseCommand):
    help = 'Parses application looking for mixpanel events.'


    def handle(self, *args, **options):

        print "Load Players!!!!1!"

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

                    if p['active'] == 'False':
                        pass

                    p['team'] = t
                    p['uniform_number'] = p['uniform_number'] or 0
                    del p['team_id']
                    del p['league_id']

                    pp.pprint(p)

                    player, created = Player.objects.get_or_create(ss_id=p['ss_id'])
                    player.update(**p)
                    player.save()

                page = page + 1
