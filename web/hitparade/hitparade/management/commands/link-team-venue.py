import pprint

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.utils import get_venues,get_key_or_null
from hitparade.models import Team, Venue
import traceback
import sys
class Command(BaseCommand):
    help = 'Link Team and Venue'

    # Not every team cleanly maps with lat/long
    team_map = {
        'Astros': 'Houston',
        'Rangers': 'Arlington',
    }

    def handle(self, *args, **options):
        pp = pprint.PrettyPrinter(indent=2)
        venues = Venue.objects.all()
        venue_name = {}
        venue_city = {}
        sr_venues_, sr_venue_cities_, sr_venue_names_ = get_venues()
        for v in venues:
            if not v.city is None:
                venue_city[v.city] = v
                venue_city[v.city.lower()] = v
            if not v.abbreviation is None:
                venue_name[v.abbreviation] = v
                venue_name[v.abbreviation.lower()] = v

        print "Link Teams and Venues!!!!1!"
        teams = Team.objects.all()
        for t in teams:
            if t.nickname in self.team_map.keys():
                venue = Venue.objects.filter(city=self.team_map[t.nickname])
            else:
                venue = Venue.objects.filter(longitude=t.longitude, latitude=t.latitude)
                if len(venue) == 0:
                    venue = Venue.objects.filter(city=t.name)
            try:
                if len(venue) == 0:
                    venue = venue_name[t.nickname]
                    if venue is None:
                        venue = venue_city[t.location]
                        if not venue is None:
                            t.venue = venue
                else:
                    t.venue = venue[0]
                sr_venue = sr_venue_names_[t.nickname.lower()]
                if sr_venue is None:
                    sr_venue = sr_venue_cities_[t.location.lower()]

                if not sr_venue is None and not venue is None:
                    venue['distances_lf'] = get_key_or_null(sr_venue, 'distances_lf')
                    venue['distances_lcf'] = get_key_or_null(sr_venue, 'distances_lcf')
                    venue['distances_cf'] = get_key_or_null(sr_venue, 'distances_cf')
                    venue['distances_rcf'] = get_key_or_null(sr_venue, 'distances_rcf')
                    venue['distances_rf'] = get_key_or_null(sr_venue, 'distances_rf')
                    venue['distances_mlf'] = get_key_or_null(sr_venue, 'distances_mlf')
                    venue['distances_mlcf'] = get_key_or_null(sr_venue, 'distances_mlcf')
                    venue['distances_mrcf'] = get_key_or_null(sr_venue, 'distances_mrcf')
                    venue['distances_mrf'] = get_key_or_null(sr_venue, 'distances_mrf')
                    print("Set distances for venue...")
                else:
                    if sr_venue is None:
                        print('sr venue is none')
                    if venue is None:
                        print('venue is None')
                t.save()
            except Exception as e:
                print e
