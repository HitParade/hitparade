from django.db import models
from django_mysql.models import Model
from django_mysql.models.fields.json import JSONField
from model_utils.models import TimeStampedModel
from utils import convert_camel2snake


class HitparadeModel(Model, TimeStampedModel):


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


    # TODO: Fully implement
    def update_from_ss(self):

        if not self.id or not self.ss_id:
            raise AmbiguousForeignKeysError()


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


class Player(HitparadeModel):
    __name__ = "Player"

    team = models.ForeignKey(Team, null=True)
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
    name = models.CharField(max_length=256, null=True)
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


class Official(HitparadeModel):
    __name__ = "Official"


    ss_id = models.CharField(max_length=36, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    uniform_number = models.IntegerField(blank=True, null=True)


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


class GameStat(HitparadeModel):
    __name__ = "GameStat"


    @staticmethod
    def get_team_ref(key, team_code):
        slug = "mlb-%s" % GameStat.team_map[team_code]
        slug = slug.lower()

        return convert_camel2snake(key), Team.objects.get(slug=slug).id


    @staticmethod
    def get_player_ref(key, player_name):
        print player_name

        player = Player.objects.get(name=player_name)

        key = u'player'

        if not player:
            print player_name
            return key, None
        else:
            return key, player.id


    @staticmethod
    def get_umpire_ref(key, official_name):
        official = Official.objects.get(name=official_name)

        key = convert_camel2snake(key)

        if not official:
            print official_name
            return key, None
        else:
            return key, official.id


    @staticmethod
    def get_venue_ref(key, venue_name):
        venue = Venue.objects.get(name=venue_name)

        key = convert_camel2snake(key)

        if not venue:
            print venue_name
            return key, None
        else:
            return key, venue.id

    key_map = {

        u'Team': get_team_ref.__func__,
        u'Opp': get_team_ref.__func__,
        u'HomeTeam': get_team_ref.__func__,
        u'HPUmp': get_umpire_ref.__func__,
        u'OppCat': get_player_ref.__func__,
        u'OppPit': get_player_ref.__func__,
        u'PlayerName': get_player_ref.__func__,
        u'Stadium': get_venue_ref.__func__,

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
        u'GameDate': u'game_date',
        u'GameNum': u'game_num',
        u'H': u'h',
        u'HBP': u'hbp',
        u'HR': u'hr',
        u'Half': u'half',
        u'IBB': u'ibb',
        u'IsOppPitRHP': u'is_opp_pit_rhp',
        u'K': u'k',
        u'LocalGameTime': u'local_game_time',
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


    home_team = models.ForeignKey(Team, related_name='+', null=True)
    opp = models.ForeignKey(Team, related_name='+', null=True)
    team = models.ForeignKey(Team, related_name='game_stat', null=True)
    hp_ump = models.ForeignKey(Official, related_name='game_stat', null=True)
    opp_cat = models.ForeignKey(Player, related_name='+', null=True)
    opp_pit = models.ForeignKey(Player, related_name='+', null=True)
    player = models.ForeignKey(Player, related_name='game_stat', null=True)
    stadium = models.ForeignKey(Venue, related_name='game_stat', null=True)

    game_date = models.DateField(null=True)
    local_game_time = models.DateField(null=True)
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


def get_games_to_update():

    return Game.query.filter(Game.status.in_([Game.STATUS_IN_PROGRESS, Game.STATUS_UPCOMING]), Game.started_at < datetime.now() )
