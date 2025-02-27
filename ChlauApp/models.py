# # models.py

from flask import current_app, render_template, session, redirect, url_for, flash
from flask_login import UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable, Text
from sqlalchemy.sql import func
from sqlalchemy.exc import *
# SQLAlchemyError, IntegrityError, OperationalError
from email.policy import default
from mailbox import Message
from smtplib import SMTPException
from datetime import datetime

import logging
logger = logging.getLogger(__name__)

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
        logger.error(f'IntegrityError: {e.orig}\n{traceback.format_exc()}')
        return 'Integrity error occurred.'
    elif isinstance(e, OperationalError):
        logger.error(f'OperationalError: {e.orig}\n{traceback.format_exc()}')
        return 'Operational error occurred.'
    elif isinstance(e, ProgrammingError):
        logger.error(f'ProgrammingError: {e.orig}\n{traceback.format_exc()}')
        return 'Programming error occurred.'
    elif isinstance(e, DataError):
        logger.error(f'DataError: {e.orig}\n{traceback.format_exc()}')
        return 'Data-related error occurred.'
    elif isinstance(e, InternalError):
        logger.error(f'InternalError: {e.orig}\n{traceback.format_exc()}')
        return 'Internal database error occurred.'
    elif isinstance(e, SQLAlchemyError):
        logger.error(f'SQLAlchemyError: {e.orig}\n{traceback.format_exc()}')
        return 'A database error occurred.'
    else:
        logger.error(f'UnexpectedError: {e}\n{traceback.format_exc()}')
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
                logger.warning ('Invalid user attemped to login' )
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('auth_bp.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

##############################################
# made dropdown list dynamic by populating them with data fetched from database
''' Define the models ----

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
---'''

''' Populate the Form Field Dynamically:  Form Class ---
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from models import Category  # Import your model

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]

--'''

''' Use the Form in the View: view function ---

@app.route('/your_form', methods=['GET', 'POST'])
def your_form():
    form = MyForm()
    if form.validate_on_submit():
        # Handle form submission
        pass
    return render_template('your_template.html', form=form)

'''

''' Render the form in a Template ----
           <div class="field">
                <label class="label">{{ form.category.label }}</label>
                <div class="control">
                    <div class="select">
                        {{ form.category() }}
                    </div>
                </div>
            </div>

---------'''

##############################################
''' database properties changes (Migrate) steps 
# 1. Make changes to your model
# 2. Generate a Migration Script 
    Bash
    $ flask db migrate -m 'Add age column to user model'
# 3. Review the Migration Script
    from alembic import op
    import sqlalchemy as sa

    # Revision identifiers, used by Alembic
    revision = '<revision_id>'
    down_revision = '<previous_revision>'
    branch_labels = None
    depends_on = None

    def upgrade():
        # Add the age column to the User table
        op.add_column('user', sa.Column('age', sa.Integer(), nullable=True))

    def downgrade():
        # Remove the age column from the User table
        op.drop_column('user', 'age')

# 4. Apply the  Migration
    Bash
    $ flask db upgrade
# 5. Verify the Changes
'''


