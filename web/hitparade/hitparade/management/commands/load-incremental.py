import pprint
import datetime

from django.conf import settings
from django.core.management import call_command, base

from hitparade.models import Team, Official, Venue, Game
from hitparade.utils import get_stattleship_client, move_ssid


class Command(base.BaseCommand):
    help = 'Load the last few days / hours data'


    def handle(self, *args, **options):

        call_command('load-atbats')
        call_command('load-bis-daily')
