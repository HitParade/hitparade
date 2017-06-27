import pprint

from django.conf import settings
from django.core.management import call_command, base

from hitparade.models import Conference, Division, Team
from hitparade.utils import get_stattleship_client, move_ssid


class Command(base.BaseCommand):
    help = 'Loads initial data'


    def handle(self, *args, **options):

        print "Load All the Thingz!!!!1!"

        call_command('load-teams')
        call_command('load-players')
        call_command('load-games')
        call_command('link-team-venue')
        call_command('load-bis-historical')
        call_command('load-bis-daily', '--date 20170301')
        call_command('load-atbats')
