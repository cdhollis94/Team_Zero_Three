from main_app import db
from flask_login import UserMixin

class Account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(80)) #80 because of sha256 hash length
