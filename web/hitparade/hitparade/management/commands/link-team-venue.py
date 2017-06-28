import pprint

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import Team, Venue


class Command(BaseCommand):
    help = 'Link Team and Venue'

    # Not every team cleanly maps with lat/long
    team_map = {
        'Astros': 'Houston',
        'Rangers': 'Arlington',
    }

    def handle(self, *args, **options):

        print "Link Teams and Venues!!!!1!"
        pp = pprint.PrettyPrinter(indent=2)

        teams = Team.objects.all()

        for t in teams:

            if t.nickname in self.team_map.keys():
                venue = Venue.objects.filter(city=self.team_map[t.nickname])
            else:

                venue = Venue.objects.filter(longitude=t.longitude, latitude=t.latitude)
                if len(venue) == 0:
                    venue = Venue.objects.filter(city=t.name)

            t.venue = venue[0]
            t.save()

