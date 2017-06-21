import pprint

from django.core.mail import send_mail
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Literally just send a test email'


    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--email',
            action='store',
            dest='email',
            default=None,
            help='Email to send a test to.',
        )


    def handle(self, *args, **options):

        print "Test Emailz!!!!1!!"

        send_mail("It works!", "This will get sent through Mailgun",
                  "Anymail Sender <from@example.com>", [options['email']])
