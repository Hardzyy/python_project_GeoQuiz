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


# class country_capital_easy(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     capital = db.Column(db.String(255))


# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(1024), nullable=False)
#
#     def __init__(self, text, tags):
#         self.text = text.strip()
#         self.tags = [
#             Tag(text=tag.strip()) for tag in tags.split(',')
#         ]
#
#
# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.String(32), nullable=False)
#
#     message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
#     message = db.relationship('Message', backref=db.backref('tags', lazy=True))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
