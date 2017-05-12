from django.conf import settings
from django.test import TestCase, TransactionTestCase
from django.contrib.auth import get_user_model
from django.template import Context, Template

from types import *
from random import randint
import json

import sure

class HPUnitTestCase(TestCase):


    def create_user(self, email='testy-mctesterson@sink.sendgrid.net',
        password='password'):

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        user.save()

        return user


    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)


    def get_html_alternative(self, mail):

        for alt in mail.alternatives:
            if alt[1] == 'text/html':
                return alt[0]

        return None


    def check_header_category_exists(self, msg, category):

        msg.extra_headers.should.contain('X-SMTPAPI')
        msg_extra_headers=json.loads(msg.extra_headers['X-SMTPAPI'])

        msg_extra_headers.should.contain('category')
        msg_extra_headers['category'].should.contain(category)


    def get_csrf_from_headers(self, result):

        for header in result.headerlist:
            if header[0] == 'Set-Cookie':
                if 'csrftoken' in header[1]:
                    tokenstr = header[1].split(';')[0]
                    return tokenstr.replace('csrftoken=', '').strip()

