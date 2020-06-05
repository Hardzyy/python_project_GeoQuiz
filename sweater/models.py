from flask_login import UserMixin

from sweater import db, manager


class Europe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    capital = db.Column(db.String(255))


class Asia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    capital = db.Column(db.String(255))


class America(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    capital = db.Column(db.String(255))


class Africa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    capital = db.Column(db.String(255))


class Oceania(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    capital = db.Column(db.String(255))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)
    all_tries = db.Column(db.Integer)
    right_answers = db.Column(db.Integer)


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
