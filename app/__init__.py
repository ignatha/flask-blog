from flask import Flask
from peewee import *

app = Flask(__name__)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.index.controller import index as index
app.register_blueprint(index)

from model import *
def create_tables():
    with database:
        database.create_tables([User])

create_tables()