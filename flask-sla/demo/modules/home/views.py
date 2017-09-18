from flask import Blueprint, render_template
from flask_login import login_required

homeRoute = Blueprint(
    'home',
    __name__,
    url_prefix='/',
    template_folder='templates'
)

@homeRoute.route('/')
@login_required
def index():
    return render_template('index.html')