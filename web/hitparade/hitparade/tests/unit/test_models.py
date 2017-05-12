import os

from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

from hitparade.models import *
from hitparade.utils import *
from types import *

from hitparade.tests.helpers import HPUnitTestCase

import sure

class HPModelTestCase(HPUnitTestCase):

    def test_gamestat_team_ref(self):

        t = Team.objects.create(slug="mlb-nyy")

        key, team = GameStat.get_team_ref("TeamName", "NYA")

        key.should.equal("team_name")
        team.should.equal(t)

        key, team = GameStat.get_team_ref("TeamName", "GRIBBLE")
        team.should.equal(None)


    def test_gamestat_player_ref(self):

        t = Team.objects.create(slug="mlb-nyy")
        p = Player.objects.create(name="Jim Stark", team=t)

        key, player = GameStat.get_player_ref("player_name", "Jim Stark")

        key.should.equal("player")
        player.should.equal(p)

        key, player = GameStat.get_player_ref("player_name", "DONT EXIST")
        player.should.equal(None)


    def test_gamestat_umpire_ref(self):

        u = Official.objects.create(name="Jim Stark")

        key, official = GameStat.get_umpire_ref("HPUmp", "Jim Stark")

        key.should.equal("hp_ump")
        official.should.equal(u)


    def test_gamestat_get_venue_ref(self):

        s = Venue.objects.create(name="Jim Stark Bowl")

        key, venue = GameStat.get_venue_ref("Stadium", "Jim Stark Bowl")

        key.should.equal("stadium")
        venue.should.equal(s)


    def test_gamestat_format_game_date(self):

        dates = ["5/30/2017", "2017-05-30T18:40:00"]

        for date in dates:
            key, pdate = GameStat.format_game_date("SOMEKey", date)

            pdate.year.should.equal(2017)
            pdate.month.should.equal(5)
            pdate.day.should.equal(30)


class HPUtilTestCase(HPUnitTestCase):


    def test_get_env_var(self):

        env_var = "DJANGO_SETTINGS_MODULE"

        get_env_variable(env_var).should.equal(os.environ[env_var])

        with self.assertRaises(ImproperlyConfigured):
            get_env_variable("cant possible exist")


    def test_get_stattleship_client(self):

        get_stattleship_client()


    def test_convert_camel2snake(self):

        convert_camel2snake("GameStat").should.equal("game_stat")


    def test_move_ssid(self):

        thing = {
            "id": "poop"
        }

        thing2 = move_ssid(thing)

        thing2.keys().should.contain("ss_id")
        thing2.keys().should_not.contain("id")
