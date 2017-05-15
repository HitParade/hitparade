import os

from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

from hitparade.models import *
from hitparade.utils import *

from hitparade.tests.helpers import HPIntegrationTestCase

from django_dynamic_fixture import G, get
import sure

class HPEndpointTestCase(HPIntegrationTestCase):


    def test_teams(self):

        t = G(Team)

        resp = self.get("/v1/teams/")
        resp.status_int.should.equal(200)

        len(resp.json).should.equal(1)

