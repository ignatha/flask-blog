from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_url

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

@login.unauthorized_handler
def unauthorized():
    if request.method == 'GET':
        return redirect(login_url('auth.login', request.url))
    else:
        return dict(error=True, message="Please log in for access."), 403


from app.index.controller import index as index
from app.auth.controller import auth as auth
app.register_blueprint(index)
app.register_blueprint(auth)


from model import *
db.create_all()