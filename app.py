from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)   # Pass the main module (this file) as the main module for the application
bootstrap = Bootstrap(app)

# [FLASK TEST CODE] ----------------------------------------------------------------------------------
# To be deleted before release

@app.route('/hello-world')
def test_page():
    """
    Test route for correct flask installation; to use:
        1 - Activate virtual environment:               venv\Scripts\activate
        2 - Assign flask app:                           set FLASK_APP=app.py
        3 - Run flask:                                  flask run
        4 - Use browser to nav to:                      http://localhost:5000/hello-world
    """
    return '<h1>Hello World</h1>'

@app.route('/hello/<name>')
def test_page_dynamic(name):
    """
    Example of dynamic URL function, will format <name> 
    """
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/template/<name>')
def test_template(name):
    return render_template('test_name.html', name=name)

# ---------------------------------------------------------------------------------------------------
