import os
import json
import pprint
import datetime
import requests
import tempfile
import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import GameStat
from hitparade.utils import s3_get_file

class Command(BaseCommand):
    """Load Historical BIS Data"""


    def handle(self, *args, **options):

        print "Load BIS Historical Data!!!1!!"

        pp = pprint.PrettyPrinter(indent=2)
        json_file = "/tmp/HistData2.json"

        if not os.path.isfile(json_file):

            f = tempfile.NamedTemporaryFile(delete=False)
            key = os.path.join(settings.AWS_S3_BIS_BUCKET_BASE_KEY, settings.BIS_HISTORICAL_ZIP)

            s3_get_file(settings.AWS_S3_BIS_BUCKET_NAME, key, f)

            p = subprocess.Popen(["unzip", "-o", f.name, "-d", os.path.dirname(f.name)], stdout=subprocess.PIPE)
            p.communicate()


        with open(json_file) as data_file:
            data = json.load(data_file)

        # pp.pprint(GameStat.key_map)

        for d in data:

            # Ignore Expos data, they're no longer a team
            if d['Team'] in GameStat.teams_ignored or \
                d['Opp'] in GameStat.teams_ignored:
                continue

            pp.pprint(d)

            kwargs = {}

            for bis_key, hp_key in GameStat.key_map.iteritems():

                if callable(hp_key):
                    k, v = hp_key(bis_key, d[bis_key])
                    kwargs[k] = v
                else:
                    kwargs[hp_key] = d[bis_key]

            pp.pprint(kwargs)

            GameStat(**kwargs).save()


