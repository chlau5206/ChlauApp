'''  auth.py
'''

from os import error
from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required, current_user
#import sqlalchemy
#import sqlalchemy.exc
# from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from email.policy import default
#from mailbox import Message
# from smtplib import SMTPException

from .. import db
from .. import login_manager
from .. import mail
from ..models import User, roles_required, get_local_time, handle_exception
from . import auth_bp
from .auth_form import AuthForm

import logging
logger = logging.getLogger(__name__)

USER_ENTRY_LIMIT = 10
ROLES = ('member', 'guest', 'sa', 'dev')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():                                                      # Done
    logger.info ('Login route accessed.')

    if User.query.first() == None:   
        logger.debug('Login: User table is empty. Route to create first user.')
        return redirect(url_for("auth_bp.create_first_user")) 
    
    aform = AuthForm()
    
    if  request.method == 'POST':
        # logger.debug('Login Request POST.')
        username = request.form.get('username').casefold().strip()
        password = request.form.get('password').strip()
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            logger.info(f'user, {user.username}, logged-in.')
            login_user(user)
            return redirect(url_for('members_bp.member'))
        
        flash(f'Invalid user={username} or password', 'danger')
        logger.warning(f'Invalid user={username} or password entered.')
    else:
        logger.debug('Login request not POST')
    
    return render_template('auth_login.html', form=aform)

@auth_bp.route('/logout')
@login_required
def logout():                                                   # Done
    logger.debug ('logout route accessed.')
    logout_user()
    session.clear()  # Clear the session data
    return redirect(url_for('auth_bp.login'))

# Set session timeout for each blueprint
@auth_bp.before_request
def make_session_permanent():
    session.permanent = True
    session.permanent_session_lifetime = timedelta(minutes=15) # Set session lifetime to 15 min (15 * 60 seconds)

#  Handle session expiration and logout for each blueprint
@auth_bp.before_request
def check_session_timeout():
    if 'user_id' in session and session.permanent:
        # Check if the session has expired
        if (datetime.now() - session['last_activity']) > session.permanent_session_lifetime:
            session.pop('user_id', None)
            logout_user()
            return redirect(url_for('auth_bp.login'))
    session['last_activity'] = datetime.now()


@auth_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('sa')  # Only admins can register new users
def remove_user(id):
    logger.debug('remove user route accessed.')
    try: 
        user = User.query.get_or_404(id)
        if user.username == 'admin' and current_user.username != 'admin':  # only admin can delete admin
            raise ValueError('You cannot delete Admin.')
        else: 
            db.session.delete(user)
            db.session.commit()

    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'{error_message}', 'error')
        logger.error(f'{error_message}')


    flash('User deleted successfully!', 'success')
    logger.info('User deleted successfully!')
    return redirect(url_for('auth_bp.display_user'))

@auth_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('sa')  # Only admins can register new users
def update_user(id):
    current_app.logger.debug('update user route accessed.')
    
    try: 
        user = User.query.get_or_404(id)
        aform = AuthForm(obj=user)
        if  aform.validate_on_submit():
            username = aform.username.data.lower().strip()
            if username == 'admin' and not current_user.username : 
                raise ValueError("Only Admin can change Admin.")
                return render_template('auth/auth_update.html', form=aform, user=user)
            elif not (username.isalnum() and 2<= len(username) <= 80):
                flash('Invalid user name', 'error')
                return render_template('auth_update.html', form=aform, user=user)
            else: 
                user.username = username
            password = aform.password.data.strip()
            if not (username.isprintable() and 2 <= len(password) <= 80):
                flash('Invalid password', 'error')
                return render_template('auth_update.html', form=aform, user=user)
            else: 
                user.password = generate_password_hash(password, method='pbkdf2:sha256')
            # user.password = hashed_password
            user.role = aform.role.data

            db.session.commit()
            flash(f'User={user.username} updated successfully!', 'success')
            logger.info(f'User={user.username} updated successfully!')
            return redirect(url_for('auth_bp.display_user'))

    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'{error_message}', 'error')
        logger.error(f'{error_message}')

    
    return render_template('auth_update.html', form=aform, user=user)

@auth_bp.route('/main')
@login_required
@roles_required('sa')  # Only admins can register new users
def display_user():
    logger.debug('Manage membership route accessed.')

    aform = AuthForm()
    users = User.query.all()
    return render_template('auth_main.html', users=users, form=aform)

@auth_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('sa')  # Only admins can register new users
def register_user():
    logger.debug('register(add) route accessed')

    try: 
        current_entries = User.query.count()  # Get the current number of entries
    
        if  current_entries >= USER_ENTRY_LIMIT:
            flash('The database has reached its limit of entries. Cannot add more members.', 'danger')
            logger.warning('The database has reached its limit of entries. Cannot add more members.')
            return redirect(url_for('auth_bp.member'))

        aform = AuthForm()
    
        if  request.method == 'POST':
            username = request.form.get('username').lower().strip()
            if not (username.isalnum() and 2<= len(username) <= 80):
                flash('Invalid user name', 'error')
                return render_template('auth_register.html', form=aform )
            password = request.form.get('password').strip()
            if not username.isprintable() and 2 <= len(password) <= 80:
                flash('Invalid password', 'error')
                return render_template('auth_register.html', form=aform )
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            role = request.form.get('role')
            new_user = User(username=username, 
                            password=hashed_password, 
                            role=role)
            db.session.add(new_user)
            db.session.commit()
            
            logger.info(f'User={username} account created.')
            return redirect(url_for('members_bp.member'))
    
    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'{error_message}', 'error')
        logger.error(f'{error_message}')

    
    return render_template('auth_register.html', form=aform )


@auth_bp.route('/first', methods=['GET', 'POST'])
# first user entry
def create_first_user():
    logger.debug('register(first user) route accessed')
    # current_entries = User.query.count()  # Get the current number of entries
    
    aform = AuthForm()
    
    try: 
        if  request.method == 'POST':
            username = request.form.get('username').lower().strip()
            
            password = request.form.get('password').strip()
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            # role = request.form.get('role')
            new_user = User(username=username, 
                            password=hashed_password, 
                            role='sa')
            print (new_user)
            db.session.add(new_user)
            db.session.commit()
            logger.info('First user created.')
            return redirect(url_for('members_bp.member'))

    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'An unexpected error occurred: {error_message}', 'error')
        logger.error(f'An unexpected error occurred: {error_message}')

    return render_template('auth_first_user.html', form=aform)

""" check if a vaild password:
import re

def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#\$%\^&\*\(\)_\+]", password):
        return False, "Password must contain at least one special character."
    
    # Check for whitespace
    if re.search(r"\s", password):
        return False, "Password cannot contain whitespace."
    
    # Check for repeated characters
    if re.search(r"(.)\1\1", password):
        return False, "Password cannot contain repeated characters."
    
    return True, "Password is valid."

# Example usage
password = "MySecureP@ssw0rd"
is_valid, message = is_valid_password(password)
print(message)
"""