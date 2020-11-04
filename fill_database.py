from app import db
from models.food_group import Food_Group

def reset_tables():
    db.drop_all
    # db.create_all()
    # db.session.commit()

def fill_food_group_table():
    fg_fruits = Food_Group(fg_name='Fruit')
    fg_grains = Food_Group(fg_name='Grain')
    fg_veggie = Food_Group(fg_name='Vegetable')
    fg_protein = Food_Group(fg_name='Protein')
    fg_dairy = Food_Group(fg_name='Dairy')

    db.session.add_all([fg_fruits, fg_grains, fg_veggie, fg_protein, fg_dairy])
    #db.session.commit()