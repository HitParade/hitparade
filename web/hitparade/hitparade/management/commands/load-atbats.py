import pprint
import datetime

from django.conf import settings
from django.core.management import call_command, base
from hitparade.models import *
from hitparade.utils import get_stattleship_client, move_ssid

from hitparade.tasks import load_at_bats, debug_task

class Command(base.BaseCommand):
    help = 'Load At-Bats from Stattleship.'


    def handle(self, *args, **options):

        print "Load At Bats!!!!1!"

        call_command('load-games')

        pp = pprint.PrettyPrinter(indent=2)

        s = get_stattleship_client()
        year = datetime.datetime.now().year
        season_slug = "mlb-%i" % year
        games = Game.objects.filter(status=Game.STATUS_CLOSED, at_bats_loaded=False)

        for game in games:

            print "Submitted Game: %i" % game.id
            load_at_bats.delay(game.id)

            return
