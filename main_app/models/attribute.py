"""
Class representing the attributes table in the db
"""

# pylint: disable=maybe-no-member

from main_app import db
from .associations import ing_att_assc

class Attribute(db.Model):
    """
    Class which accesses the DB table for attributes
    """
    __tablename__ = 'attributes'
    att_id = db.Column(db.Integer, primary_key=True)                     # Unique ID, autoincrement, primary key
    att_desc = db.Column(db.String(12), unique=True, nullable=False)     # Description of the attribute
    att_pos_neg = db.Column(db.Boolean, nullable=False)                  # Bool to determine if the attribute is positive or negative

    ingredients = db.relationship('Ingredient', secondary=ing_att_assc)

    def __repr__(self):
        return '<Attribute %r>' % self.att_desc                          # What is printed when the class is queried (required)