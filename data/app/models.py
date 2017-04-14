from main import db
from sqlalchemy.dialects.postgresql import JSON


class HitparadeModel(db.Model):
    __table_args__ = {'extend_existing': True}
    __abstract__ = True


    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.abbreviation)


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


