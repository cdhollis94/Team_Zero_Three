from flask import Blueprint, render_template, request, abort
from main_app.models.ingredient import Ingredient
from main_app.models.recipe import Recipe
from main_app import db

create_recipe_bp = Blueprint('create_recipe_bp', __name__)

# queries the database for ingredients, then loads recipe builder page
@create_recipe_bp.route('/create', methods=['GET'])
def load_recipe_builder():
    fruit = Ingredient.query.filter_by(ing_fg_id=1).all()
    grain = Ingredient.query.filter_by(ing_fg_id=2).all()
    vegetable = Ingredient.query.filter_by(ing_fg_id=3).all()
    protein = Ingredient.query.filter_by(ing_fg_id=4).all()
    dairy = Ingredient.query.filter_by(ing_fg_id=5).all()
    return render_template('create_recipe_view.html', fruit=fruit, grain=grain, vegetable=vegetable, protein=protein, dairy=dairy)

# for submitting recipes
@create_recipe_bp.route('/create', methods=['POST'])
def save_recipe():
    content = request.json
    if not content:
        abort(400)

    # if the recipe name is too long, return with message
    recipe_name = content['recipe_name']
    if len(recipe_name) > 16:
        return {'message':'invalid'}
    
    # create a recipe object, add the name, default is set to 0 because it's custom recipe
    recipe = Recipe()
    recipe.name = recipe_name
    recipe.default = 0
    
    # for all the ingredients in the request, add them to this new recipe instance
    ing_ids = content['recipe_ingredients'].values()
    for id in ing_ids:
        ingredient = Ingredient.query.filter_by(ing_id=id).first()
        recipe.ingredients.append(ingredient)
    
    db.session.add(recipe)
    db.session.commit()
    
    return {}