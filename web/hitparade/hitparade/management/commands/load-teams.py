import pprint

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Conference, Division, Team
from hitparade.utils import get_stattleship_client, move_ssid


class Command(BaseCommand):
    help = 'Parses application looking for mixpanel events.'


    def handle(self, *args, **options):

        print "Load Teams!!!!1!"

        s = get_stattleship_client()
        result = s.ss_get_results(sport='baseball',
                                league='mlb',
                                per_page=40
                                )

        pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(result[0]['teams'])

        # Load conferences
        for c in result[0]['conferences']:

            c = move_ssid(c)

            conf, created = Conference.objects.get_or_create(ss_id=c['ss_id'])
            conf.update(**c)
            conf.save()


        # Load divisions
        for d in result[0]['divisions']:

            d = move_ssid(d)

            d['conference'] = Conference.objects.get(ss_id=d['conference_id'])
            del d['conference_id']

            div, created = Division.objects.get_or_create(ss_id=d['ss_id'])
            div.update(**d)
            div.save()


        # Load teams
        for t in result[0]['teams']:

            t =move_ssid(t)

            t['division'] = Division.objects.get(ss_id=t['division_id'])
            del t['division_id']

            this_team, created = Team.objects.get_or_create(ss_id=t['ss_id'])
            this_team.update(**t)
            this_team.save()

