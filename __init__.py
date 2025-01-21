""" __init__.py
The flask application package.
"""

# import os
# from dotenv import load_dotenv
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

## Check Python at lease version 3.10
if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
	print("Python 3.10 or higher is required.")
	print("You are using Python {}.{}. ".format(sys.version_info_major, sys.version_info.minor))
	sys.exit(1)    # fail. 

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__) 
    
    ''' Load configurations from environment variables
        load_dotenv()
        app.config['FLASK_APP'] = os.getenv("FLASK_APP", ) 
        app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "development") # [development | production]
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 
        app.config["DEBUG"] = os.getenv("DEBUG", "False")
        app.config["TESTING"] = os.getenv("TESTING", "True")
        app.secret_key = os.getenv('SECRET_KEY')
    '''

    app.config['FLASK_APP'] = 'views.py'
    app.config['FLASK_ENV'] = 'development'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'AlohaFriday'
    app.config["DEBUG"] = 'True'
    app.config["TESTING"] = 'False'
    app.secret_key = 'AlohaFriday'

    # Register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    db.init_app(app)

    with app.app_context():
        # from . import models
        db.create_all() # Create tables if they don't exist

    # ## User Create/login #################################
    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # User loader callback
    @login_manager.user_loader
    def loader_user(user_id):
        from . import models
        return models.User.query.get(int(user_id))

    return app


# Initialize app 
# main = create_app()

app = create_app()

from . import views, admin 