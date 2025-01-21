## admin.py
from flask import Flask, abort
from flask import render_template, redirect, url_for, request, jsonify
from datetime import datetime

# ## User Create/login #################################
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user

from . import models
from . import contactUsModule

# # LoginManager is needed for our application 
# # to be able to log in and out users
# login_manager = LoginManager()
# login_manager.init_app(app)



# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    # return models.Users.query.get(user_id)
    return user_id


from flask import Blueprint
admin = Blueprint('admin', __name__)


@admin.route("/hello/")
@admin.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )

@admin.route('/firstUser', methods=["GET", "POST"])
def firstUser():
  # If the user made a POST request, create the first user
    if request.method == "POST":
        user = Users(username=request.form.get("username").strip(),
                     password=request.form.get("password").strip())
        # Add the user to the database
        db.session.add(user)
        # Commit the changes made
        db.session.commit()
        # Once user account created, redirect them
        # to login route (created later on)
        return redirect(url_for("home"))
    # Renders sign_up template if user made a GET request
    return render_template("login.html")

@admin.route('/register', methods=["GET", "POST"])
def register():
  # If the user made a POST request, create a new user
    if request.method == "POST":
        username=request.form.get("username").strip()
        password=request.form.get("password").strip()
        if username.isalnum() and password.isalnum():
            user = Users(username, password)
            db.session.add(user)
            # Commit the changes made
            db.session.commit()
            # Once user account created, redirect them
            # to login route (created later on)
            return redirect(url_for("hello_there"))
        else: 
            error = "Invalid username or password. Either alpha or number."
        # Add the user to the database
    # Renders sign_up template if user made a GET request
    return render_template("signUp.html", error = error)

@admin.route("/login", methods=["GET","POST"])
def login():
    # If a post request was made, find the user by 
    # filtering for the username
    error = None
    if request.method == "POST":
        retry = 5
        user = Users.query.filter_by(
            username=request.form.get("username").strip()).first()
        # Check if the password entered is the 
        # same as the user's password
        if (user != None and user.password == request.form.get("password").strip()):
            # Use the login_user method to log in the user
                login_user(user)
                return redirect(url_for("hello_there", name=f"{user.username}"))
        else:
            error = 'Invalid username or password. Please try again!'

        # Redirect the user back to the home
        # (we'll create the home route in a moment)
    return render_template("login.html", error = error)

@admin.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@admin.errorhandler(404)
def not_found(e):
    return render_template("error404.html")
