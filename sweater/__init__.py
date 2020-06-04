from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__, static_folder="static")
app.secret_key = 'hardzyy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:hardzyy@localhost/geoquiz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from sweater import models, routes

db.create_all()
