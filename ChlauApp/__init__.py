"""  ChlauApp/__init__.py
The flask application package.
"""


import logging
from logging.handlers import RotatingFileHandler

import os
from dotenv import load_dotenv

from flask import Flask # , current_app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect  #

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()
FLASK_ENV = ''

#######################################
#  create Logging
def create_logger(app):
    
    # Ensure the logs directory exists
    log_directory = os.path.join(app.root_path, 'logs')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a rotating file handler
    file_handler = RotatingFileHandler(       # 10MB 
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

    return logger

def create_app():
    from .models import User, handle_exception, get_local_time
    
    if  os.path.exists('.env.development'):
        load_dotenv(dotenv_path='.env.development')
    else: 
        load_dotenv()
    
    app = Flask(__name__) 
    
    # Load configurations from environment variables
    app.config['FLASK_APP'] = os.getenv("FLASK_APP", 'runapp.py') 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    # app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    # app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    
    app.config['APP_NAME'] = os.getenv("APP_NAME", 'ChlauApp')    
    app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "production") # [development | production]
    app.config["DEBUG"] = os.getenv("DEBUG", "False") == 'True'
    app.config["TESTING"] = os.getenv("TESTING", "False") == 'True'
    app.config['PERMANENT_SESSION_LIFETIME'] = int(os.getenv('PERMANENT_SESSION_LIFETIME' , 300))  # Set session lifetime to 5 min (5 * 60 seconds)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///sys.db')
    # app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.mail_provider.com')
    # app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'nobody@mail_provider.com')
    # app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'password')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'SecretKey') 
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

    from .about import about_bp
    app.register_blueprint(about_bp, url_prefix='/about')


    from .Board import board_bp
    app.register_blueprint(board_bp, url_prefix='/board')

    # from .gallery import gallery_bp, configure_gallery
    # app.register_blueprint(gallery_bp, url_prefix='/gallery')
    # configure_gallery(app)
    # print ("Debug: register gallery. ")
    # print (gallery_bp.template_folder)
    # print (gallery_bp.static_folder)
    


    # Initialize extensions
    db.init_app(app)  # Initialize SQLAlchemy with the Flask app
    
    # Set up Flask-Migrate
    migrate.init_app(app, db)

    
    #######################################
    # Logging

    logger = create_logger(app)

    
    """ logger usage:
        # Log messages at different levels
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
    """

    ########################################
    # init database
    try: 
        
        with app.app_context():
            db.create_all() # Create tables if they don't exist
            logger.info('init: Database tables created successfully')
    except Exception as e:
        error_message = handle_exception(e) 
        logger.error (f'An unexpected SQL error occurred: {error_message}')

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

    # # ########################################
    # # # init mail 
    # mail.init_app(app)
    
    app.logger.info('Flask application has started')

    return app


################################################################
#    Main process  ---- old codes                              #
################################################################
app = create_app()
