# [IMPORT FLASK DEPENDENCIES] ----------------------------------------------------------------------------------
from flask import Flask
app = Flask(__name__)   # Pass the main module (this file) as the main module for the application


# [DATABASE INITIATION] ----------------------------------------------------------------------------------------
from flask_sqlalchemy import SQLAlchemy
db_username = 'cs361_woym'    # Enter username for database
db_password = '5012'    # Enter password for database
db_name = 'cs361_woym'   # DB name (always class number & username)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+db_username+':'+db_password+'@classmysql.engr.oregonstate.edu/'+db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# -- Import the models to be used in the DB
from main_app.models.ingredient import Ingredient
from main_app.models.attribute import Attribute
from main_app.models.associations import ing_att_assc, ing_rec_assc
from main_app.models.food_group import Food_Group
from main_app.models.account import Account
from main_app.models.recipe import Recipe
# --------------------------------------------------------------------------------------------------------------


# [BOOTSTRAP/CSS INITIATION] -----------------------------------------------------------------------------------
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)  # Initiate bootstrap to use on the templates
# --------------------------------------------------------------------------------------------------------------


# [WTForms]-----------------------------------------------------------------------------------------------------
app.config['SECRET_KEY'] = 'Texas'
# --------------------------------------------------------------------------------------------------------------


# [flask-login]-------------------------------------------------------------------------------------------------
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = ''
login_manager.login_view = 'login_bp.login'
# --------------------------------------------------------------------------------------------------------------


# [REGISTER BLUEPRINTS] ----------------------------------------------------------------------------------------
#  - Templates used to handle individual routes used for different parts of the program
from main_app.routes.test_blueprint import test_blueprint

from main_app.routes.ingredient_bp import ingredient_bp

from main_app.routes.search_page_bp import search_bp

from main_app.routes.signup_bp import signup_bp
from main_app.routes.login_bp import login_bp
from main_app.routes.login_success_bp import login_success_bp
from main_app.routes.logout_bp import logout_bp

from main_app.routes.create_recipe_bp import create_recipe_bp

app.register_blueprint(test_blueprint)
app.register_blueprint(ingredient_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)
app.register_blueprint(login_success_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(create_recipe_bp)
app.register_blueprint(search_bp)
# --------------------------------------------------------------------------------------------------------------