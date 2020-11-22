from .__init__ import *

ingredient_bp = Blueprint('ingredient_bp', __name__)

@ingredient_bp.route('/Ingredients/<ing_name>')
def view_ing_detail(ing_name):
    ingredient = Ingredient.query.filter_by(ing_name=ing_name).first()  # Get the Ingredient object from the DB
    return render_template('ingredient_view.html', ingredient=ingredient)
