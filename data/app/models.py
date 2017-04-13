from main import db
from sqlalchemy.dialects.postgresql import JSON


class Team(db.Model):
    __tablename__ = 'team'
    __name__ = 'Team'

    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(3), unique=True, index=True)
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    conference = db.Column(db.String(32))
    division = db.Column(db.String(12))
    site_name = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(32))
    full_name = db.Column(db.String(64))

    def __repr__(self):
        return '<{} {}>'.format(self.__name__, self.abbreviation)
