'''  auth.py
'''

from os import error
from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from email.policy import default
from mailbox import Message
# from smtplib import SMTPException

import logging

from .. import db
from .. import login_manager
from .. import mail
from ..models import User, roles_required, get_local_time, SQL_exception
from . import auth_bp
from .auth_form import AuthForm

logger = logging.getLogger(__name__)
USER_ENTRY_LIMIT = 50
ROLES = ('member', 'guest', 'sa')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():                                                      # Done
    logger.info ('Login route accessed.')
    
    if User.query.first() == None:   
        logger.debug('Login: User table is empty. Route to create first user.')
        return redirect(url_for("auth_bp.create_first_user")) 
    
    aform = AuthForm()
    
    if  request.method == 'POST':
        # logger.debug('Login Request POST.')
        username = request.form.get('username').lower().strip()
        password = request.form.get('password').strip()
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('members_bp.member'))
        
        flash('Invalid username or password', 'danger')
        logger.warning(f'Invalid username or password entered. [{username}]')
    else:
        logger.debug('Login request not POST')
    
    return render_template('auth/auth_login.html', form=aform)

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
    current_app.logger.debug('remove user route accessed.')

    user = User.query.get_or_404(id)
    # aform = AuthForm(obj=user)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    logger.info('User deleted successfully!')
    return redirect(url_for('auth_bp.display_user'))

@auth_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('sa')  # Only admins can register new users
def update_user(id):
    current_app.logger.debug('update user route accessed.')
    
    user = User.query.get_or_404(id)
    aform = AuthForm(obj=user)
    try: 
        if  aform.validate_on_submit():
            user.username = aform.username.data.lower().strip()
            hashed_password = generate_password_hash(aform.password.data.strip(), method='pbkdf2:sha256')
            user.password = hashed_password
            user.role =     aform.role.data
            db.session.commit()
            flash('User updated successfully!', 'success')
            logger.info('User updated successfully!')
            return redirect(url_for('auth_bp.display_user'))
    except (SQLAlchemyError, IntegrityError, OperationalError) as e:
        db.session.rollback()
        error_message = SQL_exception(e)
        flash (f'SQL commit error: {error_message}', 'error')
        logger.error (f'SQL commit error: {error_message}') 
    except Exception as exception:
        flash (f'An unexpected error occurred: {e}', 'error')
        logger.error(f'An unexpected error occurred: {e}')
    
    return render_template('auth/auth_update.html', form=aform, user=user)

@auth_bp.route('/main')
@login_required
def display_user():
    current_app.logger.debug('Manage membership route accessed.')

    aform = AuthForm()
    users = User.query.all()
    return render_template('auth/auth_main.html', users=users, form=aform)

@auth_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('sa')  # Only admins can register new users
def create_user():
    logger.debug('register(add) route accessed')

    try: 
        current_entries = User.query.count()  # Get the current number of entries
    
        if  current_entries >= USER_ENTRY_LIMIT:
            flash('The database has reached its limit of entries. Cannot add more members.', 'danger')
            return redirect(url_for('auth_bp.member'))

        aform = AuthForm()
    
        if  request.method == 'POST':
            # add_user_sub()
            username = request.form.get('username').lower().strip()
            password = request.form.get('password').strip()
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            role = request.form.get('role')
            new_user = User(username=username, 
                            password=hashed_password, 
                            role=role)
            db.session.add(new_user)
            db.session.commit()
            msg = Message(
                    f'New user, {username} created',
                    recipients = ['charles.hin.lau@gmail.com'])
            msg.body = f'New user, {username}, is created successful. \n\n', + get_local_time()
            mail.send(msg)
            return redirect(url_for('auth_bp.member'))
    

    except (SQLAlchemyError, IntegrityError, OperationalError) as e:
        db.session.rollback()
        error_message = SQL_exception(e)
        flash (f'SQL commit error: {error_message}', 'error')
        logger.error (f'SQL commit error: {error_message}')
    
    except SMTPException as e:
        flash (f"Failed to send email: {e}", "error")
        logger.error(f"Failed to send email: {e}")
    
    except Exception as exception:
        flash (f'An unexpected error occurred: {e}', 'error')
        logger.error(f'An unexpected error occurred: {e}')


    # else:
    #     logger.info('New user added successfully.')
    #     flash('New user registered successfully!', 'success')
    # finally:
    #     logger.debug('Add new user operation finished. ')
    #     return redirect(url_for('auth_bp.member'))
    
    return render_template('auth/auth_register.html', form=aform )


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
            role = request.form.get('role')
            new_user = User(username=username, 
                            password=hashed_password, 
                            role='sa')
            print (new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth_bp.member'))

    except Exception as exception:
        error_message = SQL_exception(exception)
        logger.error(f'{error_message}')
        flash (f'{error_message}', 'error')
        return redirect(url_for('main.home'))

    return render_template('auth/auth_first_user.html', form=aform)

