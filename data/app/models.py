from main import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.exc import AmbiguousForeignKeysError
from datetime import datetime

# TODO: slug should actually be ss_slug, since we may be grabbing data from sources with differing slugs.

class HitparadeModel(db.Model):
    __table_args__ = {'extend_existing': True}
    __abstract__ = True


    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


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

    game_stats = db.relationship('GameStat', backref='player',
                                lazy='dynamic')

    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.name)


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

    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.DateTime())
    local_game_time = db.Column(db.DateTime())
    home_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    opp = db.Column(db.Integer, db.ForeignKey('team.id'))
    team = db.Column(db.Integer, db.ForeignKey('team.id'))
    hp_ump = db.Column(db.Integer, db.ForeignKey('official.id'))
    opp_cat = db.Column(db.Integer, db.ForeignKey('player.id'))
    opp_pit = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.Column(db.Integer, db.ForeignKey('player.id'))
    stadium = db.Column(db.Integer, db.ForeignKey('venue.id'))
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
