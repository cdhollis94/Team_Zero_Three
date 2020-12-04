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
description = 'The carrot is a root vegetable, usually orange in color, though purple, black, red, white, and yellow cultivars exist. The roots contain high quantities of alpha- and beta-carotene, and are a good source of vitamin K and vitamin B6.'
ing_carrot = Ingredient(ing_name='Carrot', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_carrot)

link = 'https://images.pexels.com/photos/128420/pexels-photo-128420.jpeg?cs=srgb&dl=pexels-angele-j-128420.jpg&fm=jpg'
description = 'The zucchini is a summer squash, of Mesoamerican origin, which can reach nearly 1 metre (40 inches) in length, but is usually harvested when still immature at about 15 to 25 cm (6 to 10 in).'
ing_zucchini = Ingredient(ing_name='Zucchini', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_zucchini)

link = 'https://images.pexels.com/photos/3850652/pexels-photo-3850652.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
description = 'An avocado (or avocado pear or alligator pear), is botanically a large berry containing a single large seed. Avocados are commercially valuable and are cultivated in tropical and Mediterranean climates throughout the world. They have a green-skinned, fleshy body that may be pear-shaped, egg-shaped, or spherical. Commercially, they ripen after harvesting.'
ing_avacados = Ingredient(ing_name='Avocado', fg=fg_veggie, ing_desc=description, ing_pic=link)
ing_li.append(ing_avacados)

link = 'https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
description = 'An apple is an edible fruit produced by an apple tree. Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today.'
ing_apple = Ingredient(ing_name='Apple', fg=fg_fruit, ing_desc=description, ing_pic=link)
ing_li.append(ing_apple)

link = 'https://images.pexels.com/photos/1327734/pexels-photo-1327734.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Muskmelon is a species of melon that has been developed into many cultivated varieties. These include smooth-skinned varieties such as honeydew, Crenshaw, and casaba, and different netted cultivars.'
ing_melon = Ingredient(ing_name='Melon', fg=fg_fruit, ing_desc=description, ing_pic=link)
ing_li.append(ing_melon)

link = 'https://images.pexels.com/photos/112781/pexels-photo-112781.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Beef is the culinary name for meat from cattle, particularly skeletal muscle. Humans have been eating beef since prehistoric times. Beef is a source of protein and nutrients.'
ing_beef = Ingredient(ing_name='Beef', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_beef)

link = 'https://images.pexels.com/photos/5769379/pexels-photo-5769379.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Chicken is the most common type of poultry in the world. Owing to the relative ease and low cost of raising them in comparison to animals such as cattle or hogs, chickens have become prevalent throughout the cuisine of cultures around the world, and their meat has been variously adapted to regional tastes.'
ing_chicken = Ingredient(ing_name='Chicken', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_chicken)

link = 'https://images.pexels.com/photos/1927377/pexels-photo-1927377.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Pork is the culinary name for the meat of a domestic pig. It is the most commonly consumed meat worldwide, with evidence of pig husbandry dating back to 5000 BC. Pork is eaten both freshly cooked and preserved. Curing extends the shelf life of the pork products.'
ing_pork = Ingredient(ing_name='Pork', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_pork)

link = 'https://images.pexels.com/photos/38292/walnut-nut-fruit-bowl-healthy-38292.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'A walnut is the nut of any tree of the genus Juglans, particularly the Persian or English walnut, Juglans regia. A walnut is the edible seed of a drupe, and thus not a true botanical nut. It is commonly consumed as a nut.'
ing_walnut = Ingredient(ing_name='Walnut', fg=fg_protein, ing_desc=description, ing_pic=link)
ing_li.append(ing_walnut)

link = 'https://images.pexels.com/photos/248412/pexels-photo-248412.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Milk is a nutrient-rich liquid food produced by the mammary glands of mammals. It is the primary source of nutrition for young mammals, including breastfed human infants before they are able to digest solid food.'
ing_milk = Ingredient(ing_name='Milk', fg=fg_dairy, ing_desc=description, ing_pic=link)
ing_li.append(ing_milk)

link = 'https://images.pexels.com/photos/4110257/pexels-photo-4110257.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
description = 'Brown rice is a whole grain rice with the inedible outer hull removed. White rice is the same grain without the hull, the bran layer, and the cereal germ. Red rice, gold rice, and black rice are all whole rices with differently pigmented outer layers.'
ing_brownrice = Ingredient(ing_name='Brown Rice', fg=fg_grain, ing_desc=description, ing_pic=link)
ing_li.append(ing_brownrice)

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