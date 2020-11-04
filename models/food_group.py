import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)
sys.path.append(os.path.realpath('.'))

from ..app import db

class Food_Group(db.Model):
    __tablename__ = 'food_groups'
    fg_id = db.Column(db.Integer, primary_key=True)
    fg_name = db.Column(db.String(12), unique=True, nullable=False)

    def __repr__(self):
        return '<Food_group %r>' % self.name


def fill_food_group_table():
    fg_fruits = Food_Group(fg_name='Fruit')
    fg_grains = Food_Group(fg_name='Grain')
    fg_veggie = Food_Group(fg_name='Vegetable')
    fg_protein = Food_Group(fg_name='Protein')
    fg_dairy = Food_Group(fg_name='Dairy')

    db.session.add_all([fg_fruits, fg_grains, fg_veggie, fg_protein, fg_dairy])