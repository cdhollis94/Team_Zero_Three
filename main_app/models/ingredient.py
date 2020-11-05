# pylint: disable=maybe-no-member

from main_app import db
from .associations import ing_att_assc

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(12), unique=True, nullable=False)
    ing_fg_id = db.Column(db.Integer, db.ForeignKey('food_groups.fg_id'), nullable=False)

    attributes = db.relationship('Attribute', secondary=ing_att_assc)

    def __repr__(self):
        return '<Ingredient %r>' % self.ing_name

