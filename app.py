# [IMPORT FLASK DEPENDENCIES] ----------------------------------------------------------------------------------
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# [IMPORT ROUTE BLUEPRINTS] ------------------------------------------------------------------------------------
from routes.test_blueprint import test_blueprint
from routes.ingredient_bp import ingredient_bp

# [IMPORT DB MODELS] -------------------------------------------------------------------------------------------
from models.food_group import *
from models.ingredient import *

from fill_database import *

app = Flask(__name__)   # Pass the main module (this file) as the main module for the application

# [DATABASE INITIATION] ----------------------------------------------------------------------------------------
db_username = 'cs361_woym'    # Enter username for database
db_password = '5012'    # Enter password for database
db_name = 'cs361_woym'   # DB name (always class number & username)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+db_username+':'+db_password+'@classmysql.engr.oregonstate.edu/'+db_name
db = SQLAlchemy(app)
models.food_group.fill_food_group_table()
# --------------------------------------------------------------------------------------------------------------

bootstrap = Bootstrap(app)  # Initiate bootstrap to use on the templates

# [REGISTER BLUEPRINTS] ----------------------------------------------------------------------------------------
#  - Templates used to handle individual routes used for different prats of the program
app.register_blueprint(test_blueprint)
app.register_blueprint(ingredient_bp)
# --------------------------------------------------------------------------------------------------------------

# [RUN APP] ----------------------------------------------------------------------------------------------------
port_number = 5136  # Run the app from terminal 'python3 app.py', change port number iof already in use
if __name__ == "__main__":
    app.run(port=port_number)
# --------------------------------------------------------------------------------------------------------------