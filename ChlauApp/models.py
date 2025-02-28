# # models.py
import os, sqlalchemy, smtplib
import pytz
import logging

from flask import current_app, render_template, session, redirect, url_for, flash
from flask_login import UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.exc import  SQLAlchemyError, IntegrityError, OperationalError,ProgrammingError,DataError, InternalError
from email.policy import default
from mailbox import Message
from smtplib import SMTPException
from datetime import datetime


logger = logging.getLogger(__name__)

# from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    # from flask_login import UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(10), nullable=False)    # Add role field
    __table_args__ = (
        CheckConstraint("username = LOWER(username)", name='check_username_lowercase'),
    )

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role}', password='{self.password}')>"


def get_local_time():

    local_timezone = pytz.timezone('America/Los_Angeles') 
    utc_time = datetime.utcnow()
    local_time = utc_time.astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')

    return local_time

from functools import wraps
def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if  current_user.role not in roles:
                logger.warning ('User access the page is not permissed.' )
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('members_bp.member'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def handle_exception(e):  # first version
    SQLE = (SQLAlchemyError, IntegrityError, OperationalError, 
            ProgrammingError, DataError,InternalError)

    if isinstance(e, IOError):
        return "I/O exception: {}".format(e)
    elif isinstance(e, smtplib.SMTPException):
        return "SMTP exception: {}".format(e.strerror)
    elif isinstance(e, SQLE):
        db.session.rollback()
        logger.warning('database session rollback.')
        return "SQL exception: {}".format(e)

    # elif isinstance(e, IntegrityError):
    #     db.session.rollback()
    #     logger.error(f'SQL IntegrityError: {e.orig}')
    #     return 'SQL Integrity exception: {}'.format(e)
    # elif isinstance(e, OperationalError):
    #     db.session.rollback()
    #     logger.error(f'SQL OperationalError: {e.orig}')
    #     return 'SQL Operational exception: {}'.format(e)
    # elif isinstance(e, ProgrammingError):
    #     db.session.rollback()
    #     logger.error(f'SQL ProgrammingError: {e.orig}')
    #     return 'SQL Programming exception: {}'.format(e)
    # elif isinstance(e, DataError):
    #     db.session.rollback()
    #     logger.error(f'SQL DataError: {e.orig}')
    #     return 'SQL Data-related exception: {}'.format(e)
    # elif isinstance(e, InternalError):
    #     db.session.rollback()
    #     logger.error(f'sQL InternalError: {e.orig}')
    #     return 'SQL Internal database exception: {}'.format(e)
    # elif isinstance(e, SQLAlchemyError):
    #     db.session.rollback()
    #     logger.error(f'SQLAlchemyError: {e.orig}')
    #     return 'SQL database exception: {}'.format(e)
    else:
        logger.error(f'UnexpectedError: {e}')
        return "An unexpected exception: {}".format(e)


# Example usage
# try:
#     # Some code that might raise an exception
#     raise IOError("File not found")
# except Exception as e:
#     error_message = handle_exception(e)
#     print(error_message)


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


