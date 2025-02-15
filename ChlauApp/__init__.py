""" __init__.py
The flask application package.
"""

import os
from dotenv import load_dotenv
import sys
import logging

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
mail = Mail()

def create_app():
    from .models import User
    
    # Load environment variables from .env file

    load_dotenv(dotenv_path='.env')
    # load_dotenv(dotenv_path='.env.development')

    app = Flask(__name__) 
    
    # Load configurations from environment variables
    app.config['FLASK_APP'] = os.getenv("FLASK_APP", ) 
    app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "development") # [development | production]
    app.config['APP_NAME'] = os.getenv("APP_NAME")
    app.config["DEBUG"] = os.getenv("DEBUG", "False") == 'True'
    app.config["TESTING"] = os.getenv("TESTING", "True") == 'True'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///system.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.anywhere.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'nobody@anywhere.com')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'password')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'Secret') 
    app.secret_key = os.getenv('SECRET_KEY', 'Secret')

    ########################################
    # Blueprint register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from .Students import students_bp  # Import students the blueprint
    app.register_blueprint(students_bp, url_prefix='/students')  # Register the blueprint with a URL prefix

        #################
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

    ########################################
    # init database
    db.init_app(app)
    with app.app_context():
        db.create_all() # Create tables if they don't exist

    ########################################
    # ## User Create/login 
    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'

    ########################################
    # User loader callback
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))

    ########################################
    # init csrf
    csrf.init_app(app)

    # ########################################
    # # init mail 
    mail.init_app(app)
    
    return app


def initialize_database():
    from sqlalchemy import MetaData
    meta = MetaData()
    meta.reflect(bind=db.engine)
    if 'student' not in meta.tables:
        print("Table 'student' does not exist. Creating table.")
        db.create_all()
    else:
        print("Table 'student' exists.")


################
# Main process #
################
app = create_app()
Bootstrap(app)


from . import views, admin 
