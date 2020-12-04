from .__init__ import *
from flask import Markup

search_bp = Blueprint('search_bp', __name__)

# [CREATE FORM] -----------------------------------------------------------------------------------------------
class SearchForm(FlaskForm):
    """
    Form used to search for items in the DB
    """
    choices = [ ('Ingredient', 'Ingredient'),
                ('Recipe', 'Recipe')]
    select = SelectField('Search For:', choices=choices)
    search = StringField('')
# -------------------------------------------------------------------------------------------------------------

# [CREATE TABLES] ---------------------------------------------------------------------------------------------
class Results_Ingredient(Table):
    """
    Table to show the search results from a search for ingredients
    """
    rendered_image = Col("Ingredient")
    ing_name = Col("Ingredient Name")
    food_group = Col("Food Group")
    num_pos_attributes = Col("Number of Positive Attributes")
    num_neg_attributes = Col("Number of Negative Attributes")
    link = LinkCol('View Ingredient', 'ingredient_bp.view_ing_detail', url_kwargs=dict(ing_name='ing_name'))

class Results_Recipe(Table):
    """
    Table to show the search results from a search for Food Groups
    """
    name = Col("Recipe Name")
    cumulative_pos_attributes = Col("Total Number of Positive Attributes")
    cumulative_neg_attributes = Col("Total Number of Negative Attributes")
    link = LinkCol('View Recipe', 'recipe_bp.view_recipe_detail', url_kwargs=dict(name='name'))
# -------------------------------------------------------------------------------------------------------------

# [REGISTER BLUEPRINTS] ---------------------------------------------------------------------------------------
@search_bp.route('/Search', methods=['GET','POST'])
def search_page():
    """
    Route used to display search form
    """
    search_query = SearchForm(request.form)
    if request.method == 'POST':                             # If the method is POST then a search has been executed, serve results
        return render_search_results(search_query)
    else:                                                    # If the method is GET then the page is being rendered, serve without results
        return render_template('search_view.html', form=search_query, table=None)

def render_search_results(search_query):
    """
    Route used to display search results
    """
    results = []
    search_string = search_query.data['search']
    search_target = search_query.data['select']
    
    results = get_search_result(search_target, search_string)

    if results == []:
        return 'NO RESULTS FOUND'
    else:
        if search_target == 'Ingredient':
            table = Results_Ingredient(results)
        elif search_target == 'Recipe':
            table = Results_Recipe(results)
        table.border=True
        return render_template('search_view.html', form=search_query, table=table)
# -------------------------------------------------------------------------------------------------------------

# [HELPER FUNCTIONS] ------------------------------------------------------------------------------------------
def get_search_result(search_target, search_string):
    """
    Returns the search results from the database
    """
    results=[]
    if search_string == '':
        if search_target == 'Ingredient':
            results=Ingredient.query.all()
        elif search_target == 'Recipe':
            results=Recipe.query.all()
    else:
        if search_target == 'Ingredient':
            results=Ingredient.query.filter(Ingredient.ing_name.like('%'+search_string+'%')).all()
        elif search_target == 'Recipe':
            results=Recipe.query.filter(Recipe.name.like('%'+search_string+'%')).all()
    return results
# -------------------------------------------------------------------------------------------------------------