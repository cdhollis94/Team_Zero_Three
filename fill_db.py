# pylint: disable=maybe-no-member

from main_app.models.food_group import Food_Group
from main_app.models.ingredient import Ingredient
from main_app.models.attribute import Attribute
from main_app.models.account import Account
from main_app.models.recipe import Recipe
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
link = 'https://images.pexels.com/photos/143133/pexels-photo-143133.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260'
description = ''
ing_carrot = Ingredient(ing_name='Carrot', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_carrot)

link = 'https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?cs=srgb&dl=pexels-angele-j-128420.jpg&fm=jpg'
description = ''
ing_zucchini = Ingredient(ing_name='Zucchini', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_zucchini)

link = 'https://images.pexels.com/photos/3850652/pexels-photo-3850652.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
description = ''
ing_avacados = Ingredient(ing_name='Avocado', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_avacados)

link = 'https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
description = ''
ing_apple = Ingredient(ing_name='Apple', fg=fg_fruit, ing_desc=description, ing_pic=link)
ing_li.append(ing_apple)

link = 'https://images.pexels.com/photos/1327734/pexels-photo-1327734.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_melon = Ingredient(ing_name='Melon', fg=fg_fruit, ing_desc=description, ing_pic=link)
ing_li.append(ing_melon)

link = 'https://images.pexels.com/photos/112781/pexels-photo-112781.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_beef = Ingredient(ing_name='Beef', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_beef)

link = 'https://images.pexels.com/photos/5769379/pexels-photo-5769379.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_chicken = Ingredient(ing_name='Chicken', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_chicken)

link = 'https://images.pexels.com/photos/1927377/pexels-photo-1927377.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_pork = Ingredient(ing_name='Pork', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_pork)

link = 'https://images.pexels.com/photos/38292/walnut-nut-fruit-bowl-healthy-38292.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_walnut = Ingredient(ing_name='Walnut', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_walnut)

link = 'https://images.pexels.com/photos/248412/pexels-photo-248412.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = ''
ing_milk = Ingredient(ing_name='Milk', fg=fg_dairy, ing_desc=description, ing_pic=link)
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
    for ing in ing_li:
        db.session.add(ing)
    db.session.commit()

if __name__ == "__main__":
    db.drop_all()   # Drop all the tables in the DB to make new ones
    db.create_all()     # Create all tables in the DB
    add_data()
    db.session.commit()