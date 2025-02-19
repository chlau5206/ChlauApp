""" __init__.py
The flask application package.
"""

import os
from dotenv import load_dotenv
import sys
import logging
from logging.handlers import RotatingFileHandler

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

    # load_dotenv(dotenv_path='.env')
    load_dotenv(dotenv_path='.env.development')

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
    
    print (f"FLASK_ENV = {app.config['FLASK_ENV']}")
    
    ########################################
    # Blueprint register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # from .message import message_bp
    # app.register_blueprint(message_bp, url_prefix='/message')

    # from .Students import students_bp  # Import students the blueprint
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
    db.init_app(app)
    with app.app_context():
        db.create_all() # Create tables if they don't exist

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

    Bootstrap(app)
    print ("Bootstrap() completed.")

    
    return app


################################################################
#    Main process                                              #
################################################################
app = create_app()
print("setup completed.")


from . import views # , admin 
