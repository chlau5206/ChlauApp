''' Flask web page -- views.py
'''
# from . import main
from flask import render_template #, redirect, url_for, request, jsonify, abort
from flask_login import current_user, login_required
from datetime import datetime

# from . import db                # Import the db object from __init__.py 
from . import FormModule   # contactUsModule import contactForm
# from . import models            # Import the model from __init__.py
# from .models import User
from . import admin

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)


##############
# Main Route #
##############

@main.route("/")
@main.route("/home")
def home():
    # users = models.User.query.all()
    return render_template("home.html")
main.add_url_rule('/', 'home', home)

@main.route("/about/")
def about():
    return render_template("about.html")

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    cform = FormModule.contactForm()
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

@main.route("/member")
@login_required
def member():
    # current_user
    return render_template(
        "member.html",
        name=current_user.username,
        date=datetime.now()
    )
    

