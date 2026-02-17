''' main.views.py
'''

import os
from flask import render_template,  current_app

from .AppAdmin.members.LoginForms import LoginForm   # contactUsModule import contactForm
from .utils.utilities import handle_SQL_exception

import logging
logger = logging.getLogger(__name__)

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)

# from flask import request, abort, send_from_directory, request, redirect, url_for, flash, session
# from sqlalchemy import inspect
# from flask_wtf import FlaskForm
# from datetime import datetime
# from os import error
# from . import db

##############
# Main Route #
##############

@main.route("/")
@main.route("/home/")
def home():      # Completed
    logger.debug("Home route accessed")
    return render_template("home.html", 
                           title="Home page", 
                           app_name = current_app.config['APP_NAME']
                           )

# @main.route("/about/")
# def about():     # completed
#     return render_template("about.html", title="about")

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    logger.info ("Contact us route accessed")
    cform = LoginForm.contactForm()
    return render_template("contact.html", 
                           title="Contact Me",
                           form=cform)




