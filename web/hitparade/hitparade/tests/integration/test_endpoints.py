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
import random
import sure

class HPEndpointTestCase(HPIntegrationTestCase):


    def test_teams(self):

        t = G(Team)

        resp = self.get("/v1/teams/")
        resp.status_int.should.equal(200)

        resp.json.should.have.key('next')
        resp.json.should.have.key('previous')

        resp.json['count'].should.equal(1)
        len(resp.json['results']).should.equal(1)


    def test_games(self):

        g  = G(Game, status=Game.STATUS_UPCOMING)
        g2 = G(Game, status=Game.STATUS_CLOSED)

        resp = self.get("/v1/games/")
        resp.status_int.should.equal(200)

        resp.json.should.have.key('next')
        resp.json.should.have.key('previous')

        resp.json['count'].should.equal(1)
        len(resp.json['results']).should.equal(1)
        resp.json['results'][0]['status'].should.equal(Game.STATUS_UPCOMING)

        resp = self.get("/v1/games/?status=%s" % Game.STATUS_CLOSED)
        resp.json['results'][0]['status'].should.equal(Game.STATUS_CLOSED)


    def test_players(self):

        t = G(Team)
        p = G(Player, team=t)

        resp = self.get("/v1/players/")
        resp.status_int.should.equal(200)

        resp.json.should.have.key('next')
        resp.json.should.have.key('previous')

        resp.json['count'].should.equal(1)
        len(resp.json['results']).should.equal(1)

        non_existant_team_id = random.randrange(0, 1000000)
        resp = self.get("/v1/players/?team_id=%i" % non_existant_team_id)
        len(resp.json['results']).should.equal(0)

