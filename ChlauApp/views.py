''' main.views.py
'''

import os
from flask import render_template,  current_app, url_for

from .AppAdmin.members.LoginForms import LoginForm   # contactUsModule import contactForm

import logging
logger = logging.getLogger(__name__)

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)

##############
# Main Route #
##############

@main.route("/")
@main.route("/home2/")
def home():      
    logger.debug("Home route accessed")
    return render_template("home2.html", 
                           title="Home (v2)",
                           app_name = current_app.config['APP_NAME']
                           )

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    logger.info ("Contact us route accessed")
    cform = LoginForm.contactForm()
    return render_template("contact.html", 
                           title="Contact Me",
                           form=cform)

@main.context_processor
def inject_year():
    from datetime import datetime
    return {'current_year': datetime.now().year}
