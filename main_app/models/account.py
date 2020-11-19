from main_app import db
from flask_login import UserMixin

class Account(UserMixin, db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(80)) #80 because of sha256 hash length
