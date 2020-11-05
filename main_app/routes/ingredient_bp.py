"""
[INGREDIENT BLUEPRINT] Blueprint to be used for routes handling the individual ingredient 
pages. 
"""
from flask import Blueprint, render_template

ingredient_bp = Blueprint('ingredient_bp', __name__)