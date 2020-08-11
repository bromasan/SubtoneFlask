from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    spotify_access = db.Column(db.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class BigArtist(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    genre1 = db.Column(db.String(64))
    genre2 = db.Column(db.String(64))
    genre3 = db.Column(db.String(64))
    danceability = db.Column(db.Numeric(precision=10, scale=7))
    energy = db.Column(db.Numeric(precision=10, scale=7))
    key = db.Column(db.Numeric(precision=10, scale=7))
    loudness = db.Column(db.Numeric(precision=10, scale=7))
    mode = db.Column(db.Numeric(precision=10, scale=7))
    speechiness = db.Column(db.Numeric(precision=10, scale=7))
    acousticness = db.Column(db.Numeric(precision=10, scale=7))
    instrumentalness = db.Column(db.Numeric(precision=10, scale=7))
    liveness = db.Column(db.Numeric(precision=10, scale=7))
    valence = db.Column(db.Numeric(precision=10, scale=7))
    tempo = db.Column(db.Numeric(precision=10, scale=7))

    def __repr__(self):
        return '<BigArtist {}>'.format(self.name)



class SmallArtist(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    genre1 = db.Column(db.String(64))
    genre2 = db.Column(db.String(64))
    genre3 = db.Column(db.String(64))
    danceability = db.Column(db.Numeric(precision=10, scale=7))
    energy = db.Column(db.Numeric(precision=10, scale=7))
    key = db.Column(db.Numeric(precision=10, scale=7))
    loudness = db.Column(db.Numeric(precision=10, scale=7))
    mode = db.Column(db.Numeric(precision=10, scale=7))
    speechiness = db.Column(db.Numeric(precision=10, scale=7))
    acousticness = db.Column(db.Numeric(precision=10, scale=7))
    instrumentalness = db.Column(db.Numeric(precision=10, scale=7))
    liveness = db.Column(db.Numeric(precision=10, scale=7))
    valence = db.Column(db.Numeric(precision=10, scale=7))
    tempo = db.Column(db.Numeric(precision=10, scale=7))

    def __repr__(self):
        return '<SmallArtist {}>'.format(self.name)
