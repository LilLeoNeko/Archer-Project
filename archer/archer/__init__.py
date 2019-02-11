from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='4616baa48f683f54366db8f7e824f9ea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///archer.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)

from archer import route