from flask import Blueprint, render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from main_app import db
from .search_tables import Results_Ingredient
from .search_tables import Results_Recipe
from main_app.models.ingredient import Ingredient
from main_app.models.recipe import Recipe

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

# [REGISTER BLUEPRINTS] ----------------------------------------------------------------------------------------
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