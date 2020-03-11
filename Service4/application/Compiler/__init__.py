from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

#from application.app import app

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('MY_SECRET_KEY')
