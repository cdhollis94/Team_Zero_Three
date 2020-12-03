from .__init__ import *
from .search_page_bp import Results_Ingredient

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/Recipe/<name>')
def view_recipe_detail(name):
    recipe = Recipe.query.filter_by(name=name).first()  # Get the Recipe object from the DB
    table = Results_Ingredient(recipe.ingredients)
    table.border=True
    return render_template('recipe_view.html', recipe=recipe, table=table)