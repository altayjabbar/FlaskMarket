from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '903c162071705e436c72fcf7'


db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)  
login_manager.login_view = 'login_page'  
login_manager.login_message_category = 'info'  


from market.models import User, Item
from market import routes


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  


with app.app_context():
    db.create_all()
