"""  ChlauApp/__init__.py
The flask application package.
"""
from flask import Flask # , current_app
from .extensions import db, migrate, csrf, login_manager

import logging
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)

# from flask_sqlalchemy import SQLAlchemy

from .utils.utilities import handle_SQL_exception

import os
from dotenv import load_dotenv

FLASK_ENV = ''

#######################################
#  create Logging
def create_logger(app):
    
    # Ensure the logs directory exists
    log_directory = os.path.join(app.root_path, 'logs')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory, exist_ok=True)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create a rotating file handler
    file_handler =  RotatingFileHandler(       # 10MB 
                        os.path.join(log_directory, 'app.log'), 
                        maxBytes=10*1024*1024, 
                        backupCount=5
                        )
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

def get_pacific_time():
    import pytz
    from datetime import datetime

    pacific = pytz.timezone('PST8PDT') 
    utc_time = datetime.utcnow()
    pacific_time = pytz.utc.localize(utc_time).astimezone(pacific).strftime('%Y-%m-%d %H:%M:%S')

    return pacific_time

def create_app():
    
    
    app = Flask(__name__) 

    #################################################
    # Load configurations from environment variables
    if  os.path.exists('.env.development'):
        load_dotenv(dotenv_path='.env.development')
        print ('load env.development')
    else: 
        load_dotenv()
        print ('load env (Production)')

    app.config['FLASK_APP'] = os.getenv("FLASK_APP", 'runapp.py') 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    app.config['APP_NAME'] = os.getenv("APP_NAME", 'ChlauApp')    
    app.config['FLASK_ENV'] = os.getenv("FLASK_ENV", "production") # [development | production]
    app.config["DEBUG"] = os.getenv("DEBUG", "False") == 'True'
    app.config["TESTING"] = os.getenv("TESTING", "False") == 'True'
    app.config['PERMANENT_SESSION_LIFETIME'] = int(os.getenv('PERMANENT_SESSION_LIFETIME' , 300))  # Set session lifetime to 5 min (5 * 60 seconds)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///sys.db')    # READ db
    app.config["SQLALCHEMY_BINDS"] = {'demo': 'sqlite:///:memory:'}  # DEMO db :  In-memory database
    
    # Debug
    # app.config["SQLALCHEMY_BINDS"] = {'demo': 'sqlite:///demo.db'}  # DEMO db :  debug
    app.config["WTF_CSRF_ENABLED"] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'SecretKey') 
    app.secret_key = app.config['SECRET_KEY']

    #######################################
    # Logging
    logger = create_logger(app)
    logger.info("Logging started.")
    # logger.info(f"DEBug = {app.config['DEBUG']}")
    FLASK_ENV = {app.config['FLASK_ENV']}
    if app.config['DEBUG']:
        logger.debug (f"App Name = {os.getenv('APP_NAME')}")
        logger.debug(f"FLASK_ENV={FLASK_ENV}")
    
    """ logger usage:
        # Log messages at different levels
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
    """
    
    logger.info("App begin init.")

    
    ########################################
    # Initialize extensions
    db.init_app(app)  # Initialize SQLAlchemy with the Flask app

    login_manager.init_app(app)

    # Set up Flask-Migrate
    # migrate.init_app(app, db)
    try: 
        # with app.app_context():
        #     db.create_all() # Create tables if they don't exist
        
        # Import all models here
        from .AppAdmin.members.models import User
        from .AppAdmin.adminBoard.BoardModels import Board
        

        # debug
        print("DB Type:", type(db))

        migrate.init_app(app, db) #Bind SQLAlchemy to the app
        logger.info('Bind SQLAlchemy to the app')
        
        # Creates the demo tables manually
        with app.app_context():
            from .Projects.BoardDemo.BoardDemoModels import BoardDemoTbl
            db.create_all(bind_key='demo')
            # db.create_all(bind='demo')   # incorrect syntax

            # debug
            print (db.metadata.tables.keys())  #verify table created

             # Seed demo data
            from .Projects.BoardDemo.demoBoard import seed_demo_messages
            seed_demo_messages()

            logger.info('Demo db table created.')

    except Exception as e:
        error_message = handle_SQL_exception(e) 
        logger.error (f'An unexpected SQL error occurred: {error_message}')

    logger.info("Database init completed.")

    ########################################
    # init csrf
    csrf.init_app(app)
    if app.config['DEBUG']:
        logger.debug(f'csrf exempt={csrf._exempt_views}') 
        logger.debug(f'csrf token= {csrf._get_csrf_token}')

    logger.info ('CSRF init completed.')
    
    from .AppAdmin.members.models import User #, handle_exception
    
    ########################################
    # Blueprint register views here 
    from .views import main
    app.register_blueprint(main)
    
    from .Board import board_bp
    app.register_blueprint(board_bp, url_prefix='/Board')

    from .About2 import about2_bp
    app.register_blueprint(about2_bp, url_prefix='/about')


    from .AppAdmin.members import members_bp
    app.register_blueprint(members_bp, url_prefix='/members')

    from .AppAdmin.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .AppAdmin.adminBoard import admin_board_bp
    app.register_blueprint(admin_board_bp, url_prefix='/adminBoard')
    
    
    from .Projects.ExchangeRates import exchange_rate_bp
    app.register_blueprint(exchange_rate_bp, url_prefix='/ExchangeRates')
    
    from .Projects.ePubConverter import ePubConv_bp
    app.register_blueprint(ePubConv_bp, url_prefix='/ePubConv')

    from .Projects.BoardDemo import boardDemo_bp
    app.register_blueprint(boardDemo_bp, url_prefix='/BoardDemo')

    
    from .Home2 import home2_bp
    app.register_blueprint(home2_bp, url_prefix='/home2')

    # # Old version. replace to About2
    # from .about import about_bp
    # app.register_blueprint(about_bp, url_prefix='/about')
    
    print ('Blueprint init completed.')

    ########################################
    # ## User Create/login 
    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager.login_view = 'auth_bp.login'  # old settings 'admin.login'

    ########################################
    # User loader callback
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))

    logger.info('Login manager init completed.')


    logger.info('Flask application has started')

    return app


################################################################
#    Main process  ---- old codes                              #
################################################################
app = create_app()
