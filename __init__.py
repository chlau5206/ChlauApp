""" __init__.py
The flask application package.
"""

# import os
# from dotenv import load_dotenv
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## Check Python at lease version 3.10
if not sys.version_info.major == 3 and sys.version_info.minor >= 10:
	print("Python 3.10 or higher is required.")
	print("You are using Python {}.{}. ".format(sys.version_info_major, sys.version_info.minor))
	sys.exit(1)    # fail. 

# Create the database instance
db = SQLAlchemy()

class User(db.Model):
    # from flask_login import UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

def create_app():
    app = Flask(__name__) 
    
   ## Load configurations from environment variables
    # load_dotenv()
    # app.config['FLASK_APP'] = os.getenv("FLASK_APP", ) 
    # app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "development") # [development | production]
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 
    # app.config["DEBUG"] = os.getenv("DEBUG", "False")
    # app.config["TESTING"] = os.getenv("TESTING", "True")
    # app.secret_key = os.getenv('SECRET_KEY')

    app.config['FLASK_APP'] = 'views.py'
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'AlohaFriday'
    app.config["DEBUG"] = 'True'
    app.config["TESTING"] = 'False'
    app.secret_key = 'AlohaFriday'

    db.init_app(app)

    with app.app_context():
        # from . import models
        db.create_all() # Create tables if they don't exist

    
    #     # Register views here 
    #     from .views import register_views 
    #     register_views(app)

    
    # app.register_blueprint(main)
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app


# Initialize app 
main = create_app()

from . import views
