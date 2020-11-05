from flask import Blueprint, render_template

test_blueprint = Blueprint('test_blueprint', __name__)

# [FLASK TEST CODE] ----------------------------------------------------------------------------------
# To be deleted before release

@test_blueprint.route('/hello-world')
def test_page():
    """
    Test route for correct flask installation; to use:
        1 - Activate virtual environment:               venv\Scripts\activate or source venv/bin/activate
        2 - Assign flask app:                           set FLASK_APP=app.py
        3 - Run flask:                                  flask run
        4 - Use browser to nav to:                      http://localhost:5123/hello-world
    """
    return '<h1>Hello World</h1>'

@test_blueprint.route('/hello/<name>')
def test_page_dynamic(name):
    """
    Example of dynamic URL function, will format <name> 
    """
    return '<h1>Hello, {}!</h1>'.format(name)

@test_blueprint.route('/template/<name>')
def test_template(name):
    return render_template('test_name.html', name=name)

# ---------------------------------------------------------------------------------------------------
