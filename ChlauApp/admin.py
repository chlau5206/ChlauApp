## admin.py
from flask import render_template, redirect, url_for, request, flash, session
from flask import current_app
from flask_login import current_user, login_required, login_user, logout_user

# from . import app
from . import db
from . import login_manager
from . import views
from .FormModule import LoginForm
from .models import User
from datetime import datetime

# Create Admin Blueprint
from flask import Blueprint
admin = Blueprint('admin', __name__)



@admin.route('/login', methods=['GET', 'POST'])
def login():    # completed.  May need improve login session
    current_app.logger.debug ('login route accessed.')
    current_app.logger.info ('# check empty db or new app')
    if User.query.first() == None:   
        print('User database is empty. ')
        return redirect(url_for("admin.first_user")) 

    print ('** Login route **')
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        name = loginForm.username.data.strip().lower()
        pw = loginForm.password.data.strip()
        # Here you would check the username and password against your database 
        user = User.query.filter_by(username=name).first()
        if (user and user.password == pw): # Example check 
            current_app.logger.debug ('Login successful!')
            login_user(user)
            # session['username'] = name
            return redirect(url_for("main.member"))  #, name=f"{user.username}"))
        else: 
            current_app.logger.error ('Invalid credentials.')
            return ('Error: Invalid credentials, please try again.')
    # return render_template("login.html", form=loginForm)
    
    action_URL = '/admin/login'    # It could be the root caused in Production
    return render_template("login.html", form=loginForm, action_url=action_URL)


@admin.route("/logout")
@login_required
def logout():     # completed
    current_app.logger.debug ('logout route accessed.')
    logout_user()
    # session.pop['username', None]
    return render_template('logout.html')

@admin.route('/register', methods=["GET", "POST"])
@login_required
def register():  # completed
    current_app.logger.debug ('register route accessed.')
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        name = loginForm.username.data.strip().lower()
        pw = loginForm.password.data.strip()
        # Here you would check the username and password against your database 
        user = User.query.filter_by(username=name).first()
        if user == None: # user does not exist
            new_user = User(username=name, password=pw, role='member')
            # Add the user to the database
            db.session.add(new_user)
            # Commit the changes made
            db.session.commit()
            current_app.logger.info (f'User: {name} registered successful.')
        else: 
            current_app.logger.error ( f'User {name} is already exist.')
        return redirect(url_for("main.member")) 
    else:
        current_app.logger.warn ("submit not call.")

    action_URL = '/admin/register'   # if login needed change, here needed change too.
    return render_template("sign_up.html", form=loginForm, action_url=action_URL)


@admin.route('/first_user', methods=['GET', 'POST'])
def first():      # completed
    print ('** first_user **')
    if User.query.first() == None:   # check empty db or new app
        print('User database is empty. ')
        loginForm = LoginForm()
        if loginForm.validate_on_submit():
            name = loginForm.username.data.strip().lower()
            pw = loginForm.password.data.strip()
            new_user = User(username=name, password=pw, role='sa')
            db.session.add(new_user)
            db.session.commit()
            print (f'Info: add user {name} success.')
            
            return redirect(url_for("main.member")) 
        else:
            print ("warn: submit failed.")
    
    action_URL = '/admin/first_user'
    return render_template("sign_up.html", form=loginForm, action_url=action_URL)

@admin.route("/message", methods=['GET'])
def show_messages():    # Bug: messages no show
    messages = Message.query.all()
    if messages:
        print ("No message.")
    else: 
        return render_template('messages_new.html', messages=messages)

# @admin.errorhandler(404)
# def not_found(e):
#     return render_template("error404.html")
