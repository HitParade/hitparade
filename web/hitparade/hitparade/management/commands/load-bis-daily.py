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
            dest='date',
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

        print "Load BIS Historical Daily!!!1!!"

        pp = pprint.PrettyPrinter(indent=2)

        if 'date' in options and options['date']:
            start_date = datetime.strptime(options['date'], "%Y%m%d")
        else:
            start_date = datetime.today() - timedelta(1)

        key = self.get_key(start_date)
        file = s3_get_file(settings.AWS_S3_BIS_BUCKET_NAME, key)

        while file:

            print key

            with open(file.name) as f:
                data = json.load(f)

            for d in data['Table1']:

                load_bis_game(d)

            start_date = start_date + timedelta(1)
            key = self.get_key(start_date)
            file = s3_get_file(settings.AWS_S3_BIS_BUCKET_NAME, key)
