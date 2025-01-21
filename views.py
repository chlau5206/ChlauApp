''' Flask web page -- views.py
'''
# from . import main
from flask import render_template, redirect, url_for, request, jsonify, abort

from datetime import datetime

# contactUsModule import contactForm
from . import contactUsModule
from . import models

from . import db # Import the db object from __init__.py 
from . import User # Import the model from __init__.py
from . import main

##  create Blueprint
# from flask import Blueprint
# main = Blueprint('main', __name__)

# def register_views(app):
#     app.register_blueprint(main)

##############
# Main Route #
##############

@main.route("/")
@main.route("/home")
def home():
    # items = User.query.all()
    return render_template("home.html")
# main.add_url_rule('/', 'home', home)

@main.route("/about/")
def about():
    return render_template("about.html")

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    cform = contactUsModule.contactForm()
    # if  cform.validate_on_submit(): 
    #     print(f"Name:{cform.name.data},  
    #           E-mail:{cform.email.data},  
    #           message:{cform.message.data}") 
    # else: 
    #     print("Invalid Credentials") 
    return render_template("contact.html", form=cform)

@main.route("/exchangeRate/")
def exchangeRate():
    return render_template("exchangeRate.html")


