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
from main_app.models.ingredient import Ingredient
from main_app.models.attribute import Attribute
from main_app.models.associations import ing_att_assc
from main_app.models.food_group import Food_Group
# --------------------------------------------------------------------------------------------------------------


from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)  # Initiate bootstrap to use on the templates


# [REGISTER BLUEPRINTS] ----------------------------------------------------------------------------------------
#  - Templates used to handle individual routes used for different prats of the program
from main_app.routes.test_blueprint import test_blueprint
from main_app.routes.ingredient_bp import ingredient_bp
from flask import render_template
app.register_blueprint(test_blueprint)
app.register_blueprint(ingredient_bp)
# --------------------------------------------------------------------------------------------------------------