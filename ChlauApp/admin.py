## admin.py
from flask import render_template, redirect, url_for, request, flash, session
from flask_login import current_user, login_required, login_user, logout_user

# from . import app
from . import db
from . import login_manager
from . import views
from .FormModule import LoginForm
from .models import User, Message
from datetime import datetime

# Create Admin Blueprint
from flask import Blueprint
admin = Blueprint('admin', __name__)



@admin.route('/login', methods=['GET', 'POST'])
def login():
    print ('# check empty db or new app')
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
            print ('Login successful!')
            login_user(user)
            # session['username'] = name
            return redirect(url_for("main.member"))  #, name=f"{user.username}"))
        else: 
            return ('Error: Invalid credentials, please try again.')
    # return render_template("login.html", form=loginForm)
    
    action_URL = '/admin/login'    # It could be the root caused in Production
    return render_template("login.html", form=loginForm, action_url=action_URL)


@admin.route("/logout")
@login_required
def logout():
    logout_user()
    # session.pop['username', None]
    return render_template('logout.html')

@admin.route('/register', methods=["GET", "POST"])
@login_required
def register():
    print ('** register route **')
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        name = loginForm.username.data.strip().lower()
        pw = loginForm.password.data.strip()
        # Here you would check the username and password against your database 
        user = User.query.filter_by(username=name).first()
        if user == None: # user does not exist
            new_user = User(username=name, password=pw)
            # Add the user to the database
            db.session.add(new_user)
            # Commit the changes made
            db.session.commit()
            print (f'Info: register user {name} successful.')
        else: 
            print ( f'User {name} is already exist.', 'error')
        return redirect(url_for("main.member")) 
    else:
        print ("warn: submit not call.")

    action_URL = '/admin/register'   # if login needed change, here needed change too.
    return render_template("sign_up.html", form=loginForm, action_url=action_URL)


@admin.route('/first_user', methods=['GET', 'POST'])
def first_user():
    print ('** first_user **')
    if User.query.first() == None:   # check empty db or new app
        print('User database is empty. ')
        loginForm = LoginForm()
        if loginForm.validate_on_submit():
            name = loginForm.username.data.strip().lower()
            pw = loginForm.password.data.strip()
            new_user = User(username=name, password=pw)
            db.session.add(new_user)
            db.session.commit()
            print (f'Info: add user {name} success.')
            
            return redirect(url_for("main.member")) 
        else:
            print ("warn: submit failed.")
    
    action_URL = '/admin/first_user'
    return render_template("sign_up.html", form=loginForm, action_url=action_URL)

@admin.route("/message", methods=['GET'])
def show_messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)

# @admin.errorhandler(404)
# def not_found(e):
#     return render_template("error404.html")
