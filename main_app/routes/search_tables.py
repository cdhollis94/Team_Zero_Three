from flask_table import Table, Col, LinkCol

class Results_Ingredient(Table):
    """
    Table to show the search results from a search for ingredients
    """
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
    # link = LinkCol('View Ingredient', 'ingredient_bp.view_ing_detail', url_kwargs=dict(ing_name='ing_name'))
