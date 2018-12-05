from flask import Blueprint, render_template
from flask_login import login_required

index = Blueprint('index', __name__)

@index.route('/')
@login_required
def index_route():
    return render_template("index.html")