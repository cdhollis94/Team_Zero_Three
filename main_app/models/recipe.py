from main_app import db
from .associations import ing_rec_assc

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    default = db.Column(db.Boolean) # initialize this to 1 if you're adding a default meal to the database, custom meals will be 0
    
    ingredients = db.relationship('Ingredient', secondary=ing_rec_assc)