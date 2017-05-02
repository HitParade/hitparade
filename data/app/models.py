from main import create_app
from utils import convert_camel2snake

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.exc import AmbiguousForeignKeysError
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

# TODO: slug should actually be ss_slug, since we may be grabbing data from sources with differing slugs.

app, db = create_app()

Model = declarative_base()

class HitparadeModel(db.Model):
    __table_args__ = {'extend_existing': True}
    __abstract__ = True


    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


    @staticmethod
    def create(**kwargs):

        keys_ok = set(__class__.__dict__)
        obj = __class__()

        keys_ok = set(self.__dict__)
        for k in kwargs:
            if k in keys_ok:
                setattr(obj, k, kwargs[k])

        return obj

    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.id)


    def save(self):

        if not self.id:
            db.session.add(self)

        db.session.commit()

        return self


    def update_from_ss(self):

        if not self.id or not self.ss_id:
            raise AmbiguousForeignKeysError()


class Conference(HitparadeModel):
    __tablename__ = 'conference'
    __name__ = 'Conference'

    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    name = db.Column(db.String(15))
    divisions = db.relationship('Division', backref='conference',
                                    lazy='dynamic')


class Division(HitparadeModel):
    __tablename__ = 'division'
    __name__ = 'Division'

    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    name = db.Column(db.String(36))
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    teams = db.relationship('Team', backref='division',
                                    lazy='dynamic')


class Team(HitparadeModel):
    __tablename__ = 'team'
    __name__ = 'Team'


    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    name = db.Column(db.String(64))
    slug = db.Column(db.String(7), unique=True, index=True)
    division_id = db.Column(db.Integer, db.ForeignKey('division.id'))
    location = db.Column(db.String(64))
    nickname = db.Column(db.String(64))
    colors = db.Column(db.JSON())
    hashtags = db.Column(db.JSON())
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)


class Player(HitparadeModel):
    __tablename__ = 'player'
    __name__ = "Player"

    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    slug = db.Column(db.String(64))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    active = db.Column(db.Boolean())
    # TODO: Get possible values
    bats = db.Column(db.String(12))
    birth_date = db.Column(db.DateTime())
    # TODO: get possible values
    captain = db.Column(db.String(32))
    city = db.Column(db.String(128))
    draft_overall_pick = db.Column(db.Integer())
    draft_round = db.Column(db.Integer())
    draft_season = db.Column(db.Integer())
    draft_team_name = db.Column(db.String(128))
    name = db.Column(db.String(256))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    handedness = db.Column(db.String(16))
    height = db.Column(db.Integer())
    high_school = db.Column(db.String(128))
    salary = db.Column(db.Integer())
    humanized_salary = db.Column(db.String(16))
    salary_currency = db.Column(db.String(8))
    mlbam_id = db.Column(db.Integer())
    nickname = db.Column(db.String(128))
    position_abbreviation = db.Column(db.String(8))
    position_name = db.Column(db.String(32))
    pro_debut = db.Column(db.DateTime())
    school = db.Column(db.String(64))
    state = db.Column(db.String(32))
    uniform_number = db.Column(db.Integer())
    unit_of_height = db.Column(db.String(16))
    unit_of_weight = db.Column(db.String(16))
    weight = db.Column(db.Integer())
    years_of_experience = db.Column(db.Integer())


class Official(HitparadeModel):
    __tablename__ = 'official'
    __name__ = "Official"

    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    name = db.Column(db.String(64))
    uniform_number = db.Column(db.Integer())


class Venue(HitparadeModel):
    __tablename__ = 'venue'
    __name__ = "Venue"


    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    abbreviation = db.Column(db.String(64))
    capacity = db.Column(db.Integer())
    city = db.Column(db.String(32))
    field_type = db.Column(db.String(16))
    name = db.Column(db.String(64))
    slug = db.Column(db.String(32))
    state = db.Column(db.String(2))
    stadium_type = db.Column(db.String(32))
    time_zone = db.Column(db.String(32))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)


class Game(HitparadeModel):
    __tablename__ = 'game'
    __name__ = "Game"

    STATUS_UPCOMING = "upcoming"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_CLOSED = "closed"  # ended

    STATUSES = [
        STATUS_UPCOMING,
        STATUS_IN_PROGRESS,
        STATUS_CLOSED,
    ]

    id = db.Column(db.Integer, primary_key=True)
    ss_id = db.Column(db.String(36), unique=True, index=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    winning_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    season = db.Column(db.Integer())
    at_neutral_site = db.Column(db.Boolean())
    attendance = db.Column(db.Integer())
    away_team_outcome = db.Column(db.String(16))
    away_team_score = db.Column(db.Integer())
    broadcast = db.Column(db.String(32))
    daytime = db.Column(db.Boolean())
    duration = db.Column(db.Integer())
    ended_at = db.Column(db.DateTime())
    home_team_outcome = db.Column(db.String(16))
    home_team_score = db.Column(db.Integer())
    humidity = db.Column(db.String(32))
    interval = db.Column(db.String(32))
    interval_number = db.Column(db.Integer())
    interval_type = db.Column(db.String(32))
    label = db.Column(db.String(64))
    name = db.Column(db.String(128))
    on = db.Column(db.String(64))
    period = db.Column(db.Integer())
    period_label = db.Column(db.String(16))
    score = db.Column(db.String(16))
    score_differential = db.Column(db.Integer())
    scoreline = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    started_at = db.Column(db.DateTime())
    status = db.Column(db.String(16))
    internet_coverage = db.Column(db.String(32))
    satellite_coverage = db.Column(db.String(32))
    television_coverage = db.Column(db.String(32))
    temperature = db.Column(db.String(8))
    temperature_unit = db.Column(db.String(8))
    timestamp = db.Column(db.Integer())
    title = db.Column(db.String(64))
    weather_conditions = db.Column(db.String(64))
    wind_direction = db.Column(db.String(32))
    wind_speed = db.Column(db.Integer())
    wind_speed_unit = db.Column(db.String(8))


class GameStat(HitparadeModel):
    __tablename__ = 'gamestat'
    __name__ = "Game Stat"


    @staticmethod
    def get_team_ref(key, team_code):
        slug = "mlb-%s" % GameStat.team_map[team_code]
        slug = slug.lower()

        return convert_camel2snake(key), Team.query.filter_by(slug=slug).first().id


    @staticmethod
    def get_player_ref(key, player_name):
        player = Player.query.filter_by(name=player_name).first()

        key = u'player'

        if not player:
            print player_name
            return key, None
        else:
            return key, player.id


    @staticmethod
    def get_umpire_ref(key, official_name):
        official = Official.query.filter_by(name=official_name).first()

        key = convert_camel2snake(key)

        if not official:
            print official_name
            return key, None
        else:
            return key, official.id


    @staticmethod
    def get_venue_ref(key, venue_name):
        venue = Venue.query.filter_by(name=venue_name).first()

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

    id = db.Column(db.Integer, primary_key=True)

    home_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    opp = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.Column(db.Integer, db.ForeignKey('team.id'))
    hp_ump = db.Column(db.Integer, db.ForeignKey('official.id'))
    opp_cat = db.Column(db.Integer, db.ForeignKey('player.id'))
    opp_pit = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.Column(db.Integer, db.ForeignKey('player.id'))
    stadium = db.Column(db.Integer, db.ForeignKey('venue.id'))

    game_date = db.Column(db.DateTime())
    local_game_time = db.Column(db.DateTime())
    ab = db.Column(db.Integer())
    ba14 = db.Column(db.Integer())
    ba7 = db.Column(db.Integer())
    ba_curr_month = db.Column(db.Integer())
    bb = db.Column(db.Integer())
    car_ba = db.Column(db.Float())
    car_ba_bip = db.Column(db.Float())
    car_ba_curr_month = db.Column(db.Float())
    car_ba_for_half = db.Column(db.Float())
    car_ba_in_park = db.Column(db.Float())
    car_ba_off_pit = db.Column(db.Float())
    car_ba_vs_lhp = db.Column(db.Float())
    car_ba_vs_opp = db.Column(db.Float())
    car_ba_vs_rhp = db.Column(db.Float())
    car_ba_with_ump = db.Column(db.Float())
    car_era_with_ump = db.Column(db.Float())
    car_game_num = db.Column(db.Integer())
    curr_hit_streak = db.Column(db.Integer())
    doubles = db.Column(db.Integer())
    gidp = db.Column(db.Integer())
    game_num = db.Column(db.Integer())
    h = db.Column(db.Integer())
    hbp = db.Column(db.Integer())
    hr = db.Column(db.Integer())
    half = db.Column(db.Integer())
    ibb = db.Column(db.Integer())
    is_opp_pit_rhp = db.Column(db.Integer())
    k = db.Column(db.Integer())
    opp_bullpen_era = db.Column(db.Float())
    opp_pit_car_era = db.Column(db.Float())
    opp_pit_car_l = db.Column(db.Float())
    opp_pit_car_w = db.Column(db.Float())
    opp_pit_era = db.Column(db.Float())
    opp_pit_l = db.Column(db.Integer())
    opp_pit_w = db.Column(db.Integer())
    opp_score = db.Column(db.Integer())
    pa = db.Column(db.Float())
    player_team_score = db.Column(db.Integer())
    r = db.Column(db.Integer())
    rbi = db.Column(db.Integer())
    roe = db.Column(db.Integer())
    sac = db.Column(db.Integer())
    sb = db.Column(db.Integer())
    sf = db.Column(db.Integer())
    sea_ba = db.Column(db.Float())
    sea_ba_bip = db.Column(db.Float())
    sea_ba_for_half = db.Column(db.Float())
    sea_ba_in_park = db.Column(db.Float())
    sea_ba_vs_lhp = db.Column(db.Float())
    sea_ba_vs_opp = db.Column(db.Float())
    sea_ba_vs_rhp = db.Column(db.Float())
    sea_ba_with_ump = db.Column(db.Float())
    sea_era_with_ump = db.Column(db.Float())
    triples = db.Column(db.Integer())
    was_start = db.Column(db.Integer())


def get_games_to_update():

    return Game.query.filter(Game.status.in_([Game.STATUS_IN_PROGRESS, Game.STATUS_UPCOMING]), Game.started_at < datetime.now() )
