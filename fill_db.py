# pylint: disable=maybe-no-member

from main_app.models.food_group import Food_Group
from main_app.models.ingredient import Ingredient
from main_app.models.attribute import Attribute
from main_app import db

# [INIT FGs] -----------------------------------------------------------------------------------------------------
# Create food group objects for each of the five food groups, these objects can be used to set the ingredient 
# FGs directly below due to the implementation of the 'ingredients' relationship inside the Food_Group class
fg_fruit = Food_Group(fg_name='Fruit')
fg_grain = Food_Group(fg_name='Grain')
fg_veggie = Food_Group(fg_name='Vegetable')
fg_protein = Food_Group(fg_name='Protein')
fg_dairy = Food_Group(fg_name='Dairy')

# [INIT INGs] ----------------------------------------------------------------------------------------------------
# Create a bunch of ingredients, assign food group relationship by using the variables above
ing_li = []
ing_carrot = Ingredient(ing_name='Carrot', fg=fg_veggie)
ing_li.append(ing_carrot)
ing_zucchini = Ingredient(ing_name='Zucchini', fg=fg_veggie)
ing_li.append(ing_zucchini)
ing_apple = Ingredient(ing_name='Apple', fg=fg_fruit))
ing_li.append(Ingredient(ing_name='Beef', fg=fg_protein))
ing_li.append(Ingredient(ing_name='Milk', fg=fg_dairy))

def add_data():
    db.session.add_all([fg_fruit, fg_grain, fg_veggie, fg_protein, fg_dairy])
    for ing in ing_li:
        db.session.add(ing)
    db.session.commit()

def test_db():
    print(fg_veggie.ingredients)

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    #add_data()
    #test_db()
    db.session.commit()