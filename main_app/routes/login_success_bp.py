from flask import Blueprint, render_template
from flask_login import login_required, current_user
# from main_app.models.account import Account

login_success_bp = Blueprint('login_success_bp', __name__)

@login_success_bp.route('/')
@login_required
def load_page():
    return render_template('index_view.html', username=current_user.username)