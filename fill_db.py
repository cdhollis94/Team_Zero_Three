# pylint: disable=maybe-no-member

from main_app.models.food_group import Food_Group
from main_app.models.ingredient import Ingredient
from main_app.models.attribute import Attribute
from main_app.models.account import Account
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
ing_avacados = Ingredient(ing_name='Avocado', fg=fg_veggie)
ing_li.append(ing_avacados)
ing_apple = Ingredient(ing_name='Apple', fg=fg_fruit)
ing_li.append(ing_apple)
ing_melon = Ingredient(ing_name='Melon', fg=fg_fruit)
ing_li.append(ing_melon)
ing_beef = Ingredient(ing_name='Beef', fg=fg_protein)
ing_li.append(ing_beef)
ing_chicken = Ingredient(ing_name='Chicken', fg=fg_protein)
ing_li.append(ing_chicken)
ing_pork = Ingredient(ing_name='Pork', fg=fg_protein)
ing_li.append(ing_pork)
ing_walnut = Ingredient(ing_name='Walnut', fg=fg_protein)
ing_li.append(ing_walnut)
ing_milk = Ingredient(ing_name='Milk', fg=fg_dairy)
ing_li.append(ing_milk)

# [INIT ATTs] ----------------------------------------------------------------------------------------------------
# Create a bunch of attributes, FALSE means negative and TRUE means positive attribute
att_li = []
att_1 = Attribute(att_desc="Water Intensive", att_pos_neg=False)
att_li.append(att_1)
att_2 = Attribute(att_desc="Not Water Intensive", att_pos_neg=True)
att_li.append(att_2)
att_3 = Attribute(att_desc="Prone to Animal Welfare Pitfalls",  att_pos_neg=False)
att_li.append(att_3)
att_4 = Attribute(att_desc="Often Imported; Transportation Resource Intensive", att_pos_neg=False)
att_li.append(att_4)
att_5 = Attribute(att_desc="Considered healthy, contains nutrients", att_pos_neg=True)
att_li.append(att_5)

# [LINK ATTs] ----------------------------------------------------------------------------------------------------
# Link the attributes to the ingredients
ing_avacados.attributes.append(att_1)
ing_avacados.attributes.append(att_4)
ing_avacados.attributes.append(att_5)
ing_zucchini.attributes.append(att_2)



def add_data():
    db.session.add_all([fg_fruit, fg_grain, fg_veggie, fg_protein, fg_dairy])
    for att in att_li:
        db.session.add(att)
    for ing in ing_li:
        db.session.add(ing)
    db.session.commit()

def test_db():
    print(fg_veggie.ingredients)

if __name__ == "__main__":
    db.drop_all()   # Drop all the tables in the DB to make new ones
    db.create_all()     # Create all tables in the DB
    add_data()
    #test_db()
    #db.session.commit()