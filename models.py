from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Identity

db = SQLAlchemy()

# shows = db.Table('shows',
#                  db.Column('id', db.Integer, Identity(start=1), primary_key=True),
#                  db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'), primary_key=True),
#                  db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'), primary_key=True),
#                  db.Column('start_time', db.String)
#                  )

class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    start_time = db.Column(db.String, nullable=False)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable = False)
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    past_shows = db.Column(db.String)
    past_shows_count = db.Column(db.Integer)
    upcoming_shows = db.Column(db.String)
    upcoming_shows_count = db.Column(db.Integer)
    shows = db.relationship('Show', backref='venue', lazy=True, cascade="all, delete")


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(500))
    past_shows = db.Column(db.String)
    past_shows_count = db.Column(db.Integer)
    upcoming_shows = db.Column(db.String)
    upcoming_shows_count = db.Column(db.Integer)
    shows = db.relationship('Show', backref='artist', lazy=True, cascade="all, delete")
    
