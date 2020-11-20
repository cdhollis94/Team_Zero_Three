from main_app import db
from .associations import ing_rec_assc

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    default = db.Column(db.Boolean) # initialize this to 1 if you're adding a default meal to the database, custom meals will be 0
    
    ingredients = db.relationship('Ingredient', secondary=ing_rec_assc)

    def cumulative_neg_attributes(self):
        """
        Total number of negative attributes across all ingredients
        """
        count = 0
        for ing in self.ingredients:
            for att in ing.attributes:
                if not att:
                    count += 1
        return count

    def cumulative_pos_attributes(self):
        """
        Total number of negative attributes across all ingredients
        """
        count = 0
        for ing in self.ingredients:
            for att in ing.attributes:
                if att:
                    count += 1
        return count
