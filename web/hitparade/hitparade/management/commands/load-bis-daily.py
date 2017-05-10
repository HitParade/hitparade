import os
import json
import pprint
import requests
import tempfile
import subprocess

from datetime import datetime, timedelta
from django.conf import settings
from django.core.management.base import BaseCommand

from hitparade.models import GameStat, load_bis_game
from hitparade.utils import s3_get_file

class Command(BaseCommand):
    """Load Historical BIS Data"""

    START_DATE = "20170322"

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--date',
            action='store',
            dest='start_date',
            default=None,
            help='Date from which to start import, formatted YYYYMMDD',
        )


    def format_date(self, date=None):

        if date is None:
            date = datetime.today()

        return date.strftime('%Y%m%d')


    def get_key(self, date):

        key_name = "Results_%s.json" % self.format_date(date)

        return os.path.join(settings.AWS_S3_BIS_BUCKET_BASE_KEY, key_name)


    def handle(self, *args, **options):

        print "Load BIS Daily!!!1!!"

        pp = pprint.PrettyPrinter(indent=2)
        today = datetime.today()

        if 'start_date' in options and options['start_date']:
            date = datetime.strptime(options['start_date'], "%Y%m%d")
        else:
            date = datetime.today() - timedelta(1)

        key = self.get_key(date)
        file = s3_get_file(settings.AWS_S3_BIS_BUCKET_NAME, key)

        print "Loading " + str(date)

        while date < today:

            if file:
                with open(file.name) as f:
                    data = json.load(f)

                for d in data['Table1']:
                    load_bis_game(d)

            date = date + timedelta(1)
            key = self.get_key(date)
            file = s3_get_file(settings.AWS_S3_BIS_BUCKET_NAME, key)

            print "Loading " + str(date)
