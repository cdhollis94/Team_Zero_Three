from .__init__ import *

create_recipe_bp = Blueprint('create_recipe_bp', __name__)

# table class for left column
class Ingredient_Food_Group(Table):
    """
    Table to show the ingredients for each food group
    """
    rendered_image = Col("Ingredient")
    ing_name = Col("Ingredient Name")
    food_group = Col("Food Group")
    num_pos_attributes = Col("Number of Positive Attributes")
    num_neg_attributes = Col("Number of Negative Attributes")
    
#-------------------------------------------------------------------------------

# updated when the create page is loaded. This is used to avoid requerying
# the database for ingredients when, submitting a recipe.
ingredient_storage = dict()

# queries the database for ingredients, then loads recipe builder page
@create_recipe_bp.route('/create', methods=['GET'])
def load_recipe_builder():
    # arrays of ingredients for each group from database
    fruit = Ingredient.query.filter_by(ing_fg_id=1).all()
    grain = Ingredient.query.filter_by(ing_fg_id=2).all()
    vegetable = Ingredient.query.filter_by(ing_fg_id=3).all()
    protein = Ingredient.query.filter_by(ing_fg_id=4).all()
    dairy = Ingredient.query.filter_by(ing_fg_id=5).all()

    # put in table
    fruit_table = Ingredient_Food_Group(fruit, classes=['fruit_table'])
    fruit_table.border=True
    grain_table = Ingredient_Food_Group(grain, classes=['grain_table'])
    grain_table.border=True
    vegetable_table = Ingredient_Food_Group(vegetable, classes=['vegetable_table'])
    vegetable_table.border=True
    protein_table = Ingredient_Food_Group(protein, classes=['protein_table'])
    protein_table.border=True
    dairy_table = Ingredient_Food_Group(dairy, classes=['dairy_table'])
    dairy_table.border=True

    # Server storage
    ingredient_storage.clear()
    ingredient_storage['count'] = [0, 0, 0, 0, 0]
    for f in fruit:
        ingredient_storage[f.ing_name] = f
        ingredient_storage['count'][0] += 1
    for g in grain:
        ingredient_storage[g.ing_name] = g
        ingredient_storage['count'][1] += 1
    for v in vegetable:
        ingredient_storage[v.ing_name] = v
        ingredient_storage['count'][2] += 1
    for p in protein:
        ingredient_storage[p.ing_name] = p
        ingredient_storage['count'][3] += 1
    for d in dairy:
        ingredient_storage[d.ing_name] = d
        ingredient_storage['count'][4] += 1
    
    return render_template('create_recipe_view.html',
    fruit_table=fruit_table,
    grain_table=grain_table,
    vegetable_table=vegetable_table,
    protein_table=protein_table,
    dairy_table=dairy_table,
    ing_count=ingredient_storage['count'])

# for submitting recipes
@create_recipe_bp.route('/create', methods=['POST'])
def save_recipe():
    content = request.json
    if not content:
        abort(400)

    # if the recipe name is too long, return with message
    recipe_name = content['recipe_name']
    if len(recipe_name) > 16:
        return {'message': 'invalid'}
    
    # create a recipe object, add the name, default is set to 0 because it's custom recipe
    recipe = Recipe()
    recipe.name = recipe_name
    recipe.default = 0
    
    # for all the ingredients in the request, add them to this new recipe instance
    ing_names = content['recipe_ingredients'].values()
    for ing_name in ing_names:
        ingredient = ingredient_storage[ing_name]
        recipe.ingredients.append(ingredient)
    
    db.session.add(recipe)
    db.session.commit()
    
    return {}