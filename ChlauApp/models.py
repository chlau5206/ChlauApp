# # models.py

from flask import current_app, render_template, session, redirect, url_for, flash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable, Text
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from email.policy import default
from mailbox import Message
from smtplib import SMTPException
from venv import logger
from datetime import datetime

# from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    # from flask_login import UserMixin
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(10), nullable=False)    # Add role field

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role}', password='{self.password}')>"

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime,
                          default=func.current_timestamp(),
                          onupdate=func.current_timestamp())  # Add onupdate parameter) # Add the timestamp column

    def __repr__(self):
        return f"<message {self.name[:30]} {self.email[:30]} {self.message} {self.timestamp}>"
        

def SQL_exception(e):
    if isinstance(e, IntegrityError):
        logger.error(f'IntegrityError: {e.orig}')
        return 'Integrity error occurred.'
    elif isinstance(e, OperationalError):
        logger.error(f'OperationalError: {e.orig}')
        return 'Operational error occurred.'
    elif isinstance(e, SQLAlchemyError):
        logger.error(f'SQLAlchemyError: {e.orig}')
        return 'A database error occurred.'
    else:
        logger.error(f'UnexpectedError: {e}')
        return 'An unexpected error occurred.'

def get_local_time():
    from datetime import datetime
    import pytz

    local_timezone = pytz.timezone('America/Los_Angeles') 
    utc_time = datetime.utcnow()
    local_time = utc_time.astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')

    return local_time

def roles_required(*roles):
    from functools import wraps

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if  current_user.role not in roles:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('auth_bp.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


