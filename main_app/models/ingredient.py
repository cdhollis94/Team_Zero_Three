# pylint: disable=maybe-no-member

from main_app import db
from .associations import ing_att_assc, ing_rec_assc
from .food_group import Food_Group
from flask import Markup

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(12), unique=True, nullable=False)
    ing_fg_id = db.Column(db.Integer, db.ForeignKey('food_groups.fg_id'), nullable=False)
    ing_desc = db.Column(db.String(255), unique=False, nullable=True)
    ing_pic = db.Column(db.String(255), unique=False, nullable=True)
    food_group = db.relationship('Food_Group')

    attributes = db.relationship('Attribute', secondary=ing_att_assc)
    recipes = db.relationship('Recipe', secondary=ing_rec_assc)

    def __repr__(self):
        return '<Ingredient %r>' % self.ing_name

    def num_pos_attributes(self):
        """
        Returns the number of postitive attributes belonging to the ingredient
        """
        count = 0
        for attr in self.attributes:
            if attr.att_pos_neg:
                count+=1
        return count

    def num_neg_attributes(self):
        """
        Returns the number of negative attributes belonging to the ingredient
        """
        count = 0
        for attr in self.attributes:
            if not attr.att_pos_neg:
                count+=1
        return count

    def rendered_image(self):
        """
        Wraps the image in HTML to be rendered in the table view later
        """
        html = '<img src="'+self.ing_pic+ '"width="160" height="160" alt="'+self.ing_name+ '" title="'+self.ing_name+ '" >'
        return Markup(html)