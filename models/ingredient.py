from .. import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(12), unique=True, nullable=False)
   # ing_fg_id = db.Column(db.String(12))

    def __repr__(self):
        return '<Ingredient %r>' % self.name