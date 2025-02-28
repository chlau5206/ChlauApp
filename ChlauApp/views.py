''' Flask web page -- views.py
'''
from os import error
from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required, current_user

from flask import request, json, jsonify, abort, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_wtf import FlaskForm
# from flask_login import current_user, login_required
from datetime import datetime

import os


from . import db
from . import FormModule   # contactUsModule import contactForm
from .models import get_local_time, handle_exception

import logging
logger = logging.getLogger(__name__)

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)

##############
# Main Route #
##############

@main.route("/")
@main.route("/home/")
def home():      # Completed
    logger.debug("Home route accessed")
    return render_template("home.html", 
                           title="Home page", 
                           app_name = current_app.config['APP_NAME'], 
                           today=get_local_time())

@main.route("/about/")
def about():     # completed
    return render_template("about.html", title="about")

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    logger.info ("Contact us route accessed")
    cform = FormModule.contactForm()
    return render_template("contact.html", 
                           title="Contact Us",
                           form=cform)

@main.route("/exchangeRate/")
def exchangeRate():   
    logger.debug ("Exchange Rate route accessed")
    return render_template("exchangeRate.html",
                           title="Exchange Rate")

@main.route("/loadExchangeRate")
def load_exchange_rate():
    FILE_PATH = os.path.join(current_app.root_path, 'static', 'data', 'LatestRate.json')
    try:
        ## for debug:
        # rate = '{"success":true,"timestamp":1712252526,"base":"EUR","date":"2024-09-10",
        #          "rates":{"EUR":1,"USD":1.086131,"MXN":17.932246,"SGD":1.462384,"KRW":1460.499318,"THB":39.817943,"TWD":34.789331}}'
        # data = json.loads(rate)
        # return jsonify(data)

        with open(FILE_PATH, "r") as rate:
            data = json.load(rate)   # read this file and convert the content into a Python dictionary
            logger.debug('Data loaded successfully')
        return jsonify(data)  # Use jsonify to convert the Python dictionary back into JSON format
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404  # Return a 404 error
    except json.JSONDecodeError as e:
        logger.error(f"Error in /loaddata: {e}")
        return jsonify({"error": "Invalid JSON data"}), 500  # Return a 500 error
    # except IOError as e:
    #     if not os.path.exists(os.path.dirname(FILE_PATH)): 
    #         logger.error(f'Error: The directory does not exist. {e}')
    #     else:
    #         logger.error(f'IO Error: {e}')
    except ValueError:
        logger.error("Error: Incorrect value.")
    except Exception as e:
        error_message = handle_exception(e) 
        logger.error(error_message)

