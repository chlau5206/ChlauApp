'''  auth.py
'''
from email.policy import default
from os import error
from venv import logger
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError

from .. import db
from .. import login_manager
from .. import current_app
# from .. import logging
from ..models import User
from . import auth_bp
from .auth_form import AuthForm

#import logging

ENTRY_LIMIT = 50
ROLES = ('sa', 'member', 'guest')

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if  current_user.role not in roles:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('auth_bp.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

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


@auth_bp.route('/')
@auth_bp.route('/member')
@login_required
def member():
    current_app.logger.debug('membership route accessed.')
    return render_template(
        "auth/member.html",
        title="Member",
        name=current_user.username,
        date=datetime.now()
    )


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():                                                      # Done
    logger.info ('Login route accessed.')
    
    if User.query.first() == None:   
        logger.debug('Login: User table is empty. Route to create first user.')
        return redirect(url_for("auth_bp.create_first_user")) 
    else:
        logger.debug('User table not empty.')

    aform = AuthForm()
    
    if  request.method == 'POST':
        logger.debug('Request POST.')
        username = request.form.get('username').lower().strip()
        password = request.form.get('password').strip()
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('auth_bp.member'))
        
        flash('Invalid username or password', 'danger')
        logger.warning(f'Invalid username or password entered. {username}')
    else:
        logger.debug('request not POST')
    
    return render_template('auth/auth_login.html', form=aform)

@auth_bp.route('/logout')
@login_required
def logout():                                                   # Done
    logger.debug ('logout route accessed.')
    logout_user()
    return redirect(url_for('auth_bp.login'))

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
    if  aform.validate_on_submit():
        user.username = aform.username.data
        hashed_password = generate_password_hash(aform.password.data, method='pbkdf2:sha256')
        user.password = hashed_password
        user.role =     aform.role.data
        db.session.commit()
        flash('User updated successfully!', 'success')
        logger.info('User updated successfully!')
        return redirect(url_for('auth_bp.display_user'))

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
    current_app.logger.debug('register(add) route accessed')

    try: 
        current_entries = User.query.count()  # Get the current number of entries
    
        if  current_entries >= ENTRY_LIMIT:
            flash('The database has reached its limit of entries. Cannot add more members.', 'danger')
            return redirect(url_for('auth_bp.member'))

        aform = AuthForm()
    
        if  request.method == 'POST':
            # add_user_sub()
            username = request.form.get('username').lower().strip()
            password = request.form.get('password')
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            role = request.form.get('role')
            new_user = User(username=username, 
                            password=hashed_password, 
                            role=role)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth_bp.member'))
    except Exception as exception:
        db.session.rollback()
        error_message = SQL_exception(exception)
        flash (f'{error_message}', 'error')
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
        else:
            logger.info("not POST")

    except Exception as exception:
        db.session.rollback()
        error_message = SQL_exception(exception)
        logger.error(f'{error_message}')
        flash (f'{error_message}', 'error')
        return redirect(url_for('main.home'))
    # else:
    #     logger.info('first user added successfully.')
    #     flash('First user registered successfully!', 'success')
    #     return redirect(url_for('auth_bp.login'))
    # finally:
    #     logger.debug('Add first user operation finished. ')
    #     # return redirect(url_for('auth_bp.login'))
        

    return render_template('auth/auth_first_user.html', form=aform)


# @auth_bp.route("/memberNew")
# @login_required
# def member_new():     # completed
#     # if 'username' not in session: # user not login yet
#     #     return redirect(url_for("admin.login"))
#     current_app.logger.debug ("Member route accessed")
#     return render_template(
#         "member_new.html",
#         title="Member",
#         name=current_user.username,
#         # name=session['username'],
#         date=datetime.now()
#     )
