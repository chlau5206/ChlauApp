## admin.py
# from flask import Flask, abort

from flask import render_template, redirect, url_for, request, flash, jsonify
# from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from flask_login import current_user, login_required, login_user, logout_user

# from flask_wtf import FlaskForm, CSRFProtect
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Email, InputRequired
# from . import app
from . import db
from . import login_manager
# from . import FormModule
from . import views
# from . import models
from .FormModule import LoginForm
from .models import User

# Create Admin Blueprint
from flask import Blueprint
admin = Blueprint('admin', __name__)

from datetime import datetime

# Creates a user loader callback that returns the user object given an id
# @login_manager.user_loader
# def loader_user(user_id):
#     return User.query.get(user_id)

@admin.route('/login', methods=['GET', 'POST'])
def login():
    
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        name = loginForm.username.data.strip()
        password = loginForm.password.data.strip()
        # Here you would check the username and password against your database 
        user = User.query.filter_by(username=name).first()
        if (user and user.password == password): # Example check 
            # 'Login successful!', 'success'
            login_user(user)
            return redirect(url_for("main.member"))  #, name=f"{user.username}"))
        else: 
            flash( 'Invalid credentials, please try again.', 'error')
    return render_template("login.html", form=loginForm)


@admin.route("/logout")
@login_required
def logout():
    logout_user()
    # return redirect(url_for("admin.login"))
    return render_template('logout.html')

'''
@admin.route('/register', methods=["GET", "POST"])
def register():
  # If the user made a POST request, create a new user
    if request.method == "POST":
        username=request.form.get("username").strip()
        password=request.form.get("password").strip()
        try: 
            if username.isalnum() and password.isalnum():
                user = models.User(username, password)
                db.session.add(user)
                # Commit the changes made
                db.session.commit()
                # Once user account created, redirect them
                # to login route (created later on)
                return redirect(url_for("hello_there"))
            else: 
                error = "Invalid username or password. Either alpha or number."
        except:
            print ("Error: add user failed.")
        # Add the user to the database
    # Renders sign_up template if user made a GET request
    return render_template("signUp.html", error = error)

@admin.route("/login", methods=["GET","POST"])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()
        # Here you would check the username and password against your database 
        user = User.query.filter_by(username).first()
        if (user != None and user.password == password): # Example check 
            # 'Login successful!', 'success'
            login_user(user)
            return redirect(url_for("admin.hello_there", name=f"{user.username}"))
        else: 
            error = 'Invalid credentials, please try again.'

    return render_template("login.html", form=form, error = error)

@admin.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

'''

@admin.errorhandler(404)
def not_found(e):
    return render_template("error404.html")
