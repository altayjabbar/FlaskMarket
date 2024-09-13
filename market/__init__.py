from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '903c162071705e436c72fcf7'
db = SQLAlchemy(app)

from market.models import Item 
from market import routes


with app.app_context():
    db.create_all()

