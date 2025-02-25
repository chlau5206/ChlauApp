""" __init__.py
The flask application package.
"""

import os
from sqlite3 import IntegrityError
from dotenv import load_dotenv
import sys
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_mail import Mail, Message

# from flask_bootstrap import Bootstrap

# from .models import SQL_exception
# from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
mail = Mail()
FLASK_ENV = ''

def create_app():
    from .models import User, SQL_exception, get_local_time
    # from .models import User
    
    # Load environment variables from .env file

    # load_dotenv(dotenv_path='.env')
    if  os.path.exists('.env.development'):
        load_dotenv(dotenv_path='.env.development')
    else: 
        load_dotenv()
    
    app = Flask(__name__) 
    
    # Load configurations from environment variables
    app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "production") # [development | production]
    app.config['FLASK_APP'] = os.getenv("FLASK_APP", 'runapp.py') 
    app.config['APP_NAME'] = os.getenv("APP_NAME", 'ChlauApp')
    app.config["DEBUG"] = os.getenv("DEBUG", "False") == 'True'
    app.config["TESTING"] = os.getenv("TESTING", "False") == 'True'
    app.config['PERMANENT_SESSION_LIFETIME'] = int(os.getenv('PERMANENT_SESSION_LIFETIME' , 300))  # Set session lifetime to 5 min (5 * 60 seconds)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///system.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.mail_provider.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'nobody@mail_provider.com')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'password')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'Secret') 
    app.secret_key = app.config['SECRET_KEY']
    
    print (f"App Name = {os.getenv('APP_NAME')}")
    FLASK_ENV = {app.config['FLASK_ENV']}
    print (f"{FLASK_ENV}")

    
    ########################################
    # Blueprint register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .members import members_bp
    app.register_blueprint(members_bp, url_prefix='/members')

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .Board import board_bp
    # from .ContactUs import ContactUs_bp
    app.register_blueprint(board_bp, url_prefix='/board')

    # from .students import students_bp  # Import students the blueprint
    # app.register_blueprint(students_bp, url_prefix='/students')  # Register the blueprint with a URL prefix

    ########################################
    # Logging

    # Ensure the logs directory exists
    log_directory = os.path.join(app.root_path, 'logs')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a rotating file handler
    file_handler = RotatingFileHandler(
        os.path.join(log_directory, 'app.log'), maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Create a stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    # Add handlers to the app logger
    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

    # Get the named logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    # Clear existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    ''' logger usage:
        # Log messages at different levels
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
    '''

    ########################################
    # init database
    try: 
        db.init_app(app)
        with app.app_context():
            db.create_all() # Create tables if they don't exist
    except Exception as exception:
        print (f'An unexpected SQL error occurred: {e}')



    ########################################
    # ## User Create/login 
    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'  # old settings 'admin.login'

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

    # # for bootstrap --- obs
    # Bootstrap(app)
    # print ("Bootstrap() init completed.")

    
    return app


################################################################
#    Main process                                              #
################################################################
# app = create_app()
# print("setup completed.")


# from . import views # , admin 
