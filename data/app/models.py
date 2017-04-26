from main import db
from sqlalchemy.dialects.postgresql import JSON


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
    latitude = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    longitude = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))


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


    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.name)
