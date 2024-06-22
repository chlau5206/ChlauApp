''' Flask exercise -- views.py -- 5/16/2024
'''
from . import app
from flask import Flask, abort
from flask import render_template, redirect, url_for, request, jsonify
from datetime import datetime

## User Create/login #################################
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user

# ## Custom Contact Us #########################
from flask_wtf import CSRFProtect
from flask_wtf import FlaskForm
# from wtforms import StringField, validators, PasswordField, SubmitField 
# from wtforms.validators import DataRequired, Email 
import email_validator 

# contactUsModule import contactForm
from . import contactUsModule
# from Security import KEY
KEY = "AlohaFriday"

## User Create and Login with SQLite ##############
# Tells flask-sqlalchemy what database to connect to
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# Enter a secret key
app.config["SECRET_KEY"] = KEY

# Initialize flask-sqlalchemy extension
db = SQLAlchemy()

# LoginManager is needed for our application 
# to be able to log in and out users
login_manager = LoginManager()
login_manager.init_app(app)

# Initialize app with extension
db.init_app(app)
# Create database within app context
 
with app.app_context():
    db.create_all()

# Create user model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True,
                         nullable=False)
    password = db.Column(db.String(250),
                         nullable=False)

# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

## Custom Contact Us #####################################################
app.secret_key = KEY
csrf = CSRFProtect(app)
# class contactForm(): 
#     name = StringField(label='Name', validators=[DataRequired()]) 
#     email = StringField(label='Email', 
#                         validators=[DataRequired(), Email(granular_message=True)]) 
#     message= StringField(label='Message') 
#     submit = SubmitField(label="Submit") 

#############
# Main Proc #
#############
@app.route("/")
def home():
    return render_template("home.html")
app.add_url_rule('/', 'home', home)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/", methods=["GET", "POST"])
def contact():
    cform = contactUsModule.contactForm()
    # if  cform.validate_on_submit(): 
    #     print(f"Name:{cform.name.data},  
    #           E-mail:{cform.email.data},  
    #           message:{cform.message.data}") 
    # else: 
    #     print("Invalid Credentials") 
    return render_template("contact.html", form=cform)

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )

@app.errorhandler(404)
def not_found(e):
    return render_template("error404.html")

@app.route('/firstUser', methods=["GET", "POST"])
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
    return render_template("firstUser.html")

@app.route('/register', methods=["GET", "POST"])
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

@app.route("/login", methods=["GET","POST"])
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

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/exchangeRate/")
def exchangeRate():
    return render_template("exchangeRate.html")
