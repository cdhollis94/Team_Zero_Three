"""
Class representing the food_groups table in the db
"""

# pylint: disable=maybe-no-member

from main_app import db

class Food_Group(db.Model):
    """
    Class which accesses the DB table for food groups
    """
    __tablename__ = 'food_groups'
    fg_id = db.Column(db.Integer, primary_key=True)                     # Unique ID, autoincrement, primary key
    fg_name = db.Column(db.String(12), unique=True, nullable=False)     # Name of the food group, must be unique (there should only ever be 5)

    ingredients = db.relationship('Ingredient', backref='fg')           # Notate DB relationship b/w ingredients and food group

    def __repr__(self):
        return self.fg_name                         # What is printed when the class is queried (required)