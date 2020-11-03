from .app import db

class Ingredient(db.model):
    __tablename__ = 'ingredients'
    ing_id = db.Column(db.integer, primary_key=True)
    ing_name = db.Column(db.string(12), unique=True)