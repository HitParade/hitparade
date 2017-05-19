import pprint
import dateutil.parser
import datetime
import pytz

from django.db import models
from django_mysql.models import Model
from django_mysql.models.fields.json import JSONField
from model_utils.models import TimeStampedModel
from managers import HitParadeManager
from utils import convert_camel2snake, move_ssid

class HitparadeModel(Model, TimeStampedModel):

    objects = HitParadeManager()

    class Meta:
        abstract = True


    def update(self, *args, **kwargs):

        # TODO: This should be a better exception
        if not self.id:
            raise Exception("Instance not saved yet.")

        # print "***********************update*********************"

        for attr, value in kwargs.items():
            # print attr + " : " + str(value)
            setattr(self, attr, value)

        self.save()


    @classmethod
    def create_from_ss(cls, ss_data):

        # All objects need to shift id -> ss_id
        moved_ss_data = move_ssid(ss_data)

        cleaned_ss_data = cls.clean_ss_data(moved_ss_data)

        obj, created = cls.objects.get_or_create(ss_id=cleaned_ss_data['ss_id'])
        obj.update(**cleaned_ss_data)
        obj.save()

        return obj


    def __unicode__(self):
        return self.name


class Conference(HitparadeModel):
    __name__ = 'Conference'

    ss_id = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=15)


class Division(HitparadeModel):
    __name__ = 'Division'

    ss_id = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=36)
    conference = models.ForeignKey(Conference, null=True)


class Team(HitparadeModel):
    __name__ = 'Team'


    division = models.ForeignKey(Division, null=True)
    ss_id = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=7, unique=True)
    location = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    colors = JSONField(default=list)
    hashtags = JSONField(default=list)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)


    def __unicode__(self):
        return self.nickname


class Player(HitparadeModel):
    __name__ = "Player"

    team = models.ForeignKey(Team, related_name='team', null=True)
    ss_id = models.CharField(max_length=36, unique=True)
    slug = models.CharField(max_length=64, null=True)
    active = models.NullBooleanField()
    # TODO: Get possible values
    bats = models.CharField(max_length=12)
    birth_date = models.DateField(blank=True, null=True)
    birth_date = models.DateField(null=True)
    # TODO: get possible values
    captain = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=128, null=True)
    draft_overall_pick = models.IntegerField(blank=True, null=True)
    draft_round = models.IntegerField(blank=True, null=True)
    draft_season = models.IntegerField(blank=True, null=True)
    draft_team_name = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=256, null=True, db_index=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    handedness = models.CharField(max_length=16, null=True)
    height = models.IntegerField(blank=True, null=True)
    high_school = models.CharField(max_length=128, null=True)
    salary = models.IntegerField(blank=True, null=True)
    humanized_salary = models.CharField(max_length=16, null=True)
    salary_currency = models.CharField(max_length=8, null=True)
    mlbam_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=128, null=True)
    position_abbreviation = models.CharField(max_length=8, null=True)
    position_name = models.CharField(max_length=32, null=True)
    pro_debut = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=64, null=True)
    state = models.CharField(max_length=32, null=True)
    uniform_number = models.IntegerField(blank=True, null=True)
    unit_of_height = models.CharField(max_length=16, null=True)
    unit_of_weight = models.CharField(max_length=16, null=True)
    weight = models.IntegerField(blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)


    class Meta:
        index_together = [
            ("nickname", "last_name"),
        ]


    @classmethod
    def clean_ss_data(cls, data):

        if 'team_id' in data and 'team' not in data:
            data['team'] = Team.objects.get(ss_id=data['team_id'])

        data['uniform_number'] = data['uniform_number'] or 0
        del data['team_id']
        del data['league_id']

        if not data['name'].strip():
            data['name'] = "%s %s" % (data['first_name'], data['last_name'])

        return data


class Official(HitparadeModel):
    __name__ = "Official"


    ss_id = models.CharField(max_length=36, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    uniform_number = models.IntegerField(blank=True, null=True)


    @classmethod
    def clean_ss_data(cls, data):

        data[u'uniform_number'] = data['uniform_number'] or 0

        return data


class Venue(HitparadeModel):
    __name__ = "Venue"


    ss_id = models.CharField(max_length=36, unique=True)
    abbreviation = models.CharField(max_length=64)
    capacity = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=32, null=True)
    field_type = models.CharField(max_length=16, null=True)
    name = models.CharField(max_length=64, null=True)
    slug = models.CharField(max_length=32, null=True)
    state = models.CharField(max_length=2, null=True)
    stadium_type = models.CharField(max_length=32, null=True)
    time_zone = models.CharField(max_length=32, null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)


    @classmethod
    def clean_ss_data(cls, data):
        return data


class Game(HitparadeModel):
    __name__ = "Game"

    STATUS_UPCOMING = "upcoming"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_CLOSED = "closed"  # ended

    STATUSES = [
        STATUS_UPCOMING,
        STATUS_IN_PROGRESS,
        STATUS_CLOSED,
    ]

    home_team = models.ForeignKey(Team, related_name='home_game', null=True)
    away_team = models.ForeignKey(Team, related_name='away_game', null=True)
    winning_team = models.ForeignKey(Team, related_name='winning_game', null=True)
    venue = models.ForeignKey(Venue, null=True)

    ss_id = models.CharField(max_length=36, unique=True)
    season = models.IntegerField(blank=True, null=True)
    at_bats_loaded = models.BooleanField(default=False)
    at_neutral_site = models.NullBooleanField()
    attendance = models.IntegerField(blank=True, null=True)
    away_team_outcome = models.CharField(max_length=16)
    away_team_score = models.IntegerField(blank=True, null=True)
    broadcast = models.CharField(max_length=32)
    daytime = models.NullBooleanField()
    duration = models.IntegerField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    home_team_outcome = models.CharField(max_length=16)
    home_team_score = models.IntegerField(blank=True, null=True)
    humidity = models.CharField(max_length=32, null=True)
    interval = models.CharField(max_length=32, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    interval_type = models.CharField(max_length=32)
    label = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=128, null=True)
    on = models.CharField(max_length=64, null=True)
    period = models.IntegerField(blank=True, null=True)
    period_label = models.CharField(max_length=16, null=True)
    score = models.CharField(max_length=16, null=True)
    score_differential = models.IntegerField(blank=True, null=True)
    scoreline = models.CharField(max_length=64, null=True)
    slug = models.CharField(max_length=64, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=16, null=True)
    internet_coverage = models.CharField(max_length=32, null=True)
    satellite_coverage = models.CharField(max_length=32, null=True)
    television_coverage = models.CharField(max_length=32, null=True)
    temperature = models.CharField(max_length=8, null=True)
    temperature_unit = models.CharField(max_length=8, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=64, null=True)
    weather_conditions = models.CharField(max_length=64, null=True)
    wind_direction = models.CharField(max_length=32, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_speed_unit = models.CharField(max_length=8, null=True)


    @classmethod
    def clean_ss_data(cls, data):

        data[u'home_team'] = Team.objects.get(ss_id=data['home_team_id'])
        data[u'away_team'] = Team.objects.get(ss_id=data['away_team_id'])
        data[u'venue'] = Venue.objects.get(ss_id=data['venue_id'])

        if data['winning_team_id']:
            data['winning_team'] = Team.objects.get(ss_id=data['winning_team_id'])

        del data['home_team_id']
        del data['away_team_id']
        del data['venue_id']
        del data['winning_team_id']

        return data


class GameStat(HitparadeModel):
    __name__ = "GameStat"


    @staticmethod
    def get_team_ref(key, team_code):

        # Not sure if this is the best option.
        #   If we can't find a team, we should probably raise
        if team_code not in GameStat.team_map:
            return convert_camel2snake(key), None

        slug = "mlb-%s" % GameStat.team_map[team_code]
        slug = slug.lower()

        return convert_camel2snake(key), Team.objects.get(slug=slug)


    @staticmethod
    def get_player_ref(key, value):

        if 'MLBAMId' in key:
            player = Player.objects.get_or_none(mlbam_id=value)
        else:
            player = Player.objects.get_or_none(name=value)

            # Try the nickname
            if player is None:
                split_name = value.split(" ")
                player = Player.objects.get_or_none(nickname=split_name[0], last_name=split_name[1])

        key = key.replace('MLBAMId', '')
        key = convert_camel2snake(key)

        if key == 'player_name':
            key = 'player'

        if not player:
            return key, None
        else:
            return key, player


    @staticmethod
    def get_umpire_ref(key, official_name):
        official = Official.objects.get_or_none(name=official_name)

        key = convert_camel2snake(key)

        if not official:
            return key, None
        else:
            return key, official


    @staticmethod
    def get_venue_ref(key, venue_name):
        venue = Venue.objects.get_or_none(name=venue_name)

        key = convert_camel2snake(key)

        if not venue:
            return key, None
        else:
            return key, venue


    @staticmethod
    def format_game_date(key, date):
        """BIS sends us a couple different date formats - 5/30/2011, 2017-05-05T18:40:00"""

        key = 'game_date'
        date = dateutil.parser.parse(date)
        date = pytz.utc.localize(date).date()

        if not date:
            return key, None
        else:
            return key, date


    @staticmethod
    def denaive_date(key, date):
        """Dates come in with no timezone. This matures them."""

        key = convert_camel2snake(key)
        date = dateutil.parser.parse('2017-05-05T18:40:00')
        date = pytz.utc.localize(date).date()

        if not date:
            return key, None
        else:
            return key, date


    # Both of these are here so we can continue to support older files that
    #    don't have mlbam_id
    player_key_map = {
        u'OppCat': get_player_ref.__func__,
        u'OppPit': get_player_ref.__func__,
        u'PlayerName': get_player_ref.__func__,
    }

    player_name_map = {
        # BIS          # Stattleship
        "DJ LeMahieu": "David LeMahieu"
    }

    key_map = {

        u'Team': get_team_ref.__func__,
        u'Opp': get_team_ref.__func__,
        u'HomeTeam': get_team_ref.__func__,
        u'HPUmp': get_umpire_ref.__func__,
        u'Stadium': get_venue_ref.__func__,
        u'GameDate': format_game_date.__func__,
        u'LocalGameTime': denaive_date.__func__,


        u'AB': u'ab',
        u'BA14': u'ba14',
        u'BA7': u'ba7',
        u'BACurrMonth': u'ba_curr_month',
        u'BB': u'bb',
        u'CarBA': u'car_ba',
        u'CarBABIP': u'car_ba_bip',
        u'CarBACurrMonth': u'car_ba_curr_month',
        u'CarBAForHalf': u'car_ba_for_half',
        u'CarBAInPark': u'car_ba_in_park',
        u'CarBAOffPit': u'car_ba_off_pit',
        u'CarBAVsLHP': u'car_ba_vs_lhp',
        u'CarBAVsOpp': u'car_ba_vs_opp',
        u'CarBAVsRHP': u'car_ba_vs_rhp',
        u'CarBAWithUmp': u'car_ba_with_ump',
        u'CarERAWithUmp': u'car_era_with_ump',
        u'CarGameNum': u'car_game_num',
        u'CurrHitStreak': u'curr_hit_streak',
        u'Doubles': u'doubles',
        u'GIDP': u'gidp',
        u'GameNum': u'game_num',
        u'H': u'h',
        u'HBP': u'hbp',
        u'HR': u'hr',
        u'Half': u'half',
        u'IBB': u'ibb',
        u'IsOppPitRHP': u'is_opp_pit_rhp',
        u'K': u'k',
        u'OppBullpenERA': u'opp_bullpen_era',
        u'OppPitCarERA': u'opp_pit_car_era',
        u'OppPitCarL': u'opp_pit_car_l',
        u'OppPitCarW': u'opp_pit_car_w',
        u'OppPitERA': u'opp_pit_era',
        u'OppPitL': u'opp_pit_l',
        u'OppPitW': u'opp_pit_w',
        u'OppScore': u'opp_score',
        u'PA': u'pa',
        u'PlayerTeamScore': u'player_team_score',
        u'R': u'r',
        u'RBI': u'rbi',
        u'ROE': u'roe',
        u'SAC': u'sac',
        u'SB': u'sb',
        u'SF': u'sf',
        u'SeaBA': u'sea_ba',
        u'SeaBABIP': u'sea_ba_bip',
        u'SeaBAForHalf': u'sea_ba_for_half',
        u'SeaBAInPark': u'sea_ba_in_park',
        u'SeaBAVsLHP': u'sea_ba_vs_lhp',
        u'SeaBAVsOpp': u'sea_ba_vs_opp',
        u'SeaBAVsRHP': u'sea_ba_vs_rhp',
        u'SeaBAWithUmp': u'sea_ba_with_ump',
        u'SeaERAWithUmp': u'sea_era_with_ump',
        u'Triples': u'triples',
        u'WasStart': u'was_start'
    }

    teams_ignored = [
        "ANA",
        "MON"
    ]

    team_map = {
        #BIS  : HP
        u"ANA": "LAA",
        u"ARI": "ARI",
        u"ATL": "ATL",
        u"BAL": "BAL",
        u"BOS": "BOS",
        u"CHA": "CHW",
        u"CHN": "CHC",
        u"CIN": "CIN",
        u"CLE": "CLE",
        u"COL": "COL",
        u"DET": "DET",
        u"FLA": "MIA",
        u"HOU": "HOU",
        u"KC": "KC",
        u"LA": "LA",
        u"LAN": "LA",
        u"LAA": "LAA",
        u"MIA": "MIA",
        u"MIL": "MIL",
        u"MIN": "MIN",
        # Montreal is no longer a team
        # u"MON": "",
        u"NYA": "NYY",
        u"NYN": "NYM",
        u"OAK": "OAK",
        u"PHI": "PHI",
        u"PIT": "PHI",
        u"SD": "SD",
        u"SEA": "SEA",
        u"SF": "SF",
        u"STL": "STL",
        u"TB": "TB",
        u"TEX": "TEX",
        u"TOR": "TOR",
        u"WAS": "WAS"
    }


    # TODO: Add a reference to the game model. duh.
    home_team = models.ForeignKey(Team, related_name='+', null=True)
    opp = models.ForeignKey(Team, related_name='+', null=True)
    team = models.ForeignKey(Team, related_name='game_stat', null=True)
    hp_ump = models.ForeignKey(Official, related_name='game_stat', null=True)
    opp_cat = models.ForeignKey(Player, related_name='+', null=True)
    opp_pit = models.ForeignKey(Player, related_name='+', null=True)
    player = models.ForeignKey(Player, related_name='game_stat', null=True)
    stadium = models.ForeignKey(Venue, related_name='game_stat', null=True)

    game_date = models.DateField(null=True)
    local_game_time = models.DateTimeField(null=True)
    ab = models.IntegerField(null=True)
    ba14 = models.IntegerField(null=True)
    ba7 = models.IntegerField(null=True)
    ba_curr_month = models.IntegerField(null=True)
    bb = models.IntegerField(null=True)
    car_ba = models.FloatField(null=True)
    car_ba_bip = models.FloatField(null=True)
    car_ba_curr_month = models.FloatField(null=True)
    car_ba_for_half = models.FloatField(null=True)
    car_ba_in_park = models.FloatField(null=True)
    car_ba_off_pit = models.FloatField(null=True)
    car_ba_vs_lhp = models.FloatField(null=True)
    car_ba_vs_opp = models.FloatField(null=True)
    car_ba_vs_rhp = models.FloatField(null=True)
    car_ba_with_ump = models.FloatField(null=True)
    car_era_with_ump = models.FloatField(null=True)
    car_game_num = models.IntegerField(null=True)
    curr_hit_streak = models.IntegerField(null=True)
    doubles = models.IntegerField(null=True)
    gidp = models.IntegerField(null=True)
    game_num = models.IntegerField(null=True)
    h = models.IntegerField(null=True)
    hbp = models.IntegerField(null=True)
    hr = models.IntegerField(null=True)
    half = models.IntegerField(null=True)
    ibb = models.IntegerField(null=True)
    is_opp_pit_rhp = models.IntegerField(null=True)
    k = models.IntegerField(null=True)
    opp_bullpen_era = models.FloatField(null=True)
    opp_pit_car_era = models.FloatField(null=True)
    opp_pit_car_l = models.FloatField(null=True)
    opp_pit_car_w = models.FloatField(null=True)
    opp_pit_era = models.FloatField(null=True)
    opp_pit_l = models.IntegerField(null=True)
    opp_pit_w = models.IntegerField(null=True)
    opp_score = models.IntegerField(null=True)
    pa = models.FloatField(null=True)
    player_team_score = models.IntegerField(null=True)
    r = models.IntegerField(null=True)
    rbi = models.IntegerField(null=True)
    roe = models.IntegerField(null=True)
    sac = models.IntegerField(null=True)
    sb = models.IntegerField(null=True)
    sf = models.IntegerField(null=True)
    sea_ba = models.FloatField(null=True)
    sea_ba_bip = models.FloatField(null=True)
    sea_ba_for_half = models.FloatField(null=True)
    sea_ba_in_park = models.FloatField(null=True)
    sea_ba_vs_lhp = models.FloatField(null=True)
    sea_ba_vs_opp = models.FloatField(null=True)
    sea_ba_vs_rhp = models.FloatField(null=True)
    sea_ba_with_ump = models.FloatField(null=True)
    sea_era_with_ump = models.FloatField(null=True)
    triples = models.IntegerField(null=True)
    was_start = models.IntegerField(null=True)


    def __unicode__(self):
        return "%s vs %s" % (self.home_team.name, self.team.name)

    class Meta:
        unique_together = (('player', 'car_game_num'),)


class AtBat(HitparadeModel):
    __name__ = "AtBat"

    ss_id = models.CharField(max_length=36, unique=True)

    game = models.ForeignKey(Game, related_name='at_bats', null=True)
    hitter = models.ForeignKey(Player, related_name='at_bats', null=True)
    hitter_team = models.ForeignKey(Team, related_name='+', null=True)

    description = models.CharField(max_length=256, null=True)
    half = models.CharField(max_length=2, null=True)
    inning = models.IntegerField(null=True)
    inning_label = models.CharField(max_length=32, null=True)


    def __unicode__(self):
        return "%s %s At Bat" % (self.game, self.hitter.name)


    @classmethod
    def create_from_ss(cls, ss_data):
        obj = super(AtBat, cls).create_from_ss(ss_data)

        for pitch_id in ss_data['baseball_pitch_ids']:
            pitch = Pitch.objects.get_or_none(ss_id=pitch_id)

            if pitch is not None:
                pitch.at_bat = obj
                pitch.save()

        return obj


    @classmethod
    def clean_ss_data(cls, data):

        data[u'hitter_team'] = Team.objects.get(ss_id=data['hitter_team_id'])
        data[u'hitter'] = Player.objects.get(ss_id=data['hitter_id'])

        # If game not set, grab the reference to the game object
        if 'game' not in data and 'game_id' in data:
            data['game'] = Game.objects.get(ss_id=data['game_id'])

        del data['game_id']
        del data['hitter_team_id']
        del data['hitter_id']

        return data


class Pitch(HitparadeModel):
    __name__ = "Pitch"
    verbose_name_plural = "Pitches"


    class Meta:
        verbose_name_plural = "Pitches"


    ss_id = models.CharField(max_length=36, unique=True)

    # I have no idea what an event is
    # event_id = models.IntegerField(null=True) u'e67486ff-f21e-468f-b77d-2d0781bfa297',

    at_bat = models.ForeignKey(AtBat, related_name='at_bat', null=True)
    game = models.ForeignKey(Game, related_name='pitch', null=True)
    hitter = models.ForeignKey(Player, related_name="+", null=True)
    hitter_team = models.ForeignKey(Team, related_name='+', null=True)
    pitcher = models.ForeignKey(Player, related_name='+', null=True)
    team = models.ForeignKey(Team, related_name='+', null=True)

    at_bat_balls = models.IntegerField(null=True)
    at_bat_outs = models.IntegerField(null=True)
    at_bat_pitch_count = models.IntegerField(null=True)
    at_bat_strikes = models.IntegerField(null=True)
    even_count = models.NullBooleanField()
    full_count = models.NullBooleanField()
    half = models.CharField(max_length=2, null=True)
    hit_location = models.IntegerField(null=True)
    hit_type = models.CharField(max_length=2, null=True)
    hitter_pitch_count = models.CharField(max_length=3, null=True)
    inning = models.IntegerField(null=True)
    inning_label = models.CharField(max_length=32, null=True)
    is_at_bat = models.NullBooleanField()
    is_at_bat_over = models.NullBooleanField()
    is_bunt = models.NullBooleanField()
    is_bunt_shown = models.NullBooleanField()
    is_double_play = models.NullBooleanField()
    is_hit = models.NullBooleanField()
    is_on_base = models.NullBooleanField()
    is_passed_ball = models.NullBooleanField()
    is_triple_play = models.NullBooleanField()
    is_wild_pitch = models.NullBooleanField()
    pitched_at = models.DateTimeField(null=True)
    pitch_count = models.IntegerField(null=True)
    pitch_name = models.CharField(max_length=32, null=True)
    pitch_outcome = models.CharField(max_length=32, null=True)
    pitch_outcome_type = models.CharField(max_length=32, null=True)
    pitch_speed = models.FloatField(null=True)
    pitch_type = models.CharField(max_length=8, null=True)
    pitch_zone = models.IntegerField(null=True)
    sequence = models.IntegerField(null=True)


    def __unicode__(self):
        return "%s - %s - %i" % (self.game, self.hitter.name, self.sequence)


    @classmethod
    def clean_ss_data(cls, data):

        data[u'team'] = Team.objects.get(ss_id=data['team_id'])
        data[u'hitter_team'] = Team.objects.get(ss_id=data['hitter_team_id'])
        data[u'pitcher'] = Player.objects.get(ss_id=data['pitcher_id'])
        data[u'hitter'] = Player.objects.get(ss_id=data['hitter_id'])

        data[u'pitch_zone'] = data[u'pitch_zone'] or None
        data[u'hit_location'] = data[u'hit_location'] or None

        # If game not set, grab the reference to the game object
        if 'game' not in data and 'game_id' in data:
            data['game'] = Game.objects.get(ss_id=data['game_id'])

        del data['game_id']
        del data['team_id']
        del data['hitter_team_id']
        del data['hitter_id']
        del data['pitcher_id']

        return data


def load_bis_game(data):

    pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(data)

    # Ignore Expos data, they're no longer a team
    if data['Team'] in GameStat.teams_ignored or \
        data['Opp'] in GameStat.teams_ignored:
        return

    kwargs = {}

    for bis_key, hp_key in GameStat.key_map.iteritems():

        if bis_key in data:
            if callable(hp_key):
                k, v = hp_key(bis_key, data[bis_key])
                kwargs[k] = v
            else:
                kwargs[hp_key] = data[bis_key]


    for bis_player_key, hp_player_key in GameStat.player_key_map.iteritems():

        mlbamid_key = bis_player_key + 'MLBAMId'

        if mlbamid_key in data:
            k, v = hp_player_key(mlbamid_key, data[mlbamid_key])
            kwargs[k] = v
        else:
            k, v = hp_player_key(bis_player_key, data[bis_player_key])
            kwargs[k] = v


    ga, created = GameStat.objects.get_or_create(player=kwargs['player'], car_game_num=kwargs['car_game_num'])
    ga.update(**kwargs)
    ga.save()

    return ga


def get_games_to_update():

    kwargs = {
        "status__in":[Game.STATUS_IN_PROGRESS, Game.STATUS_UPCOMING],
        "started_at__lt": datetime.datetime.now()
    }

    return Game.objects.filter(**kwargs)
