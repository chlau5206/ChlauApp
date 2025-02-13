""" __init__.py
The flask application package.
"""

# import os
# from dotenv import load_dotenv
import sys
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap

def create_app():
    from .models import User
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
    #  Flask environment [ development | production ]
    app.config['FLASK_ENV'] = 'development'  # means debug=True

    app.config['APP_NAME'] = 'Chlau5206 Web'
    app.config['FLASK_APP'] = 'runapp.py'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'AlohaFriday'
    # app.config["DEBUG"] = 'True'
    # app.config["TESTING"] = 'False'
    app.secret_key = 'AlohaFriday'

    db.init_app(app)
    with app.app_context():
        # from . import models
        db.create_all() # Create tables if they don't exist

    # ## User Create/login #################################
    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'

    # User loader callback
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))

    # Blueprint register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    # Set up logging
    log_file_path = os.path.join(app.root_path, 'logs', 'app.log')
    logging.basicConfig(filename=log_file_path, 
                        filemode='a',  # w = overwritten each time ; a = appending to the file 
                        level=logging.DEBUG, # means all levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) will be logged.
                        format='%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)


    # # Example log messages
    # logging.debug('This is a debug message')
    # logging.info('This is an info message')
    # logging.warning('This is a warning message')
    # logging.error('This is an error message')
    # logging.critical('This is a critical message')

    return app


db = SQLAlchemy()
login_manager = LoginManager()
app = create_app()
csrf = CSRFProtect(app)
Bootstrap(app)

from . import views, admin 
