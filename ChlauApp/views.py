''' Flask web page -- views.py
'''
# from . import main
from flask import current_app, render_template, session, redirect, url_for, flash
from flask import Flask,request, json, jsonify, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_wtf import FlaskForm
from flask_login import current_user, login_required
from datetime import datetime


from . import db
from . import FormModule   # contactUsModule import contactForm
from . import admin

import os

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)

##############
# Main Route #
##############

@main.route("/")
@main.route("/home/")
def home():      # Completed
    current_app.logger.debug("Home route accessed")
    # users = models.User.query.all()
    return render_template("home.html", 
                           title="Home page", 
                           app_name = current_app.config['APP_NAME'])
main.add_url_rule('/', 'home', home)

@main.route("/about/")
def about():     # completed
    return render_template("about.html", title="about")

@main.route("/contact/", methods=["GET", "POST"])
def contact():
    current_app.logger.info ("Contact us route accessed")
    cform = FormModule.contactForm()
    return render_template("contact.html", 
                           title="Contact Us",
                           form=cform)

@main.route("/exchangeRate/")
def exchangeRate():   
    current_app.logger.debug ("Exchange Rate route accessed")
    return render_template("exchangeRate.html",
                           title="Exchange Rate")

@main.route("/loadExchangeRate")
def load_exchange_rate():
    FILE_PATH = os.path.join(current_app.root_path, 'static', 'data', 'LatestRate.json')
    try:
        ## for debug:
        # rate = '{"success":true,"timestamp":1712252526,"base":"EUR","date":"2024-09-10","rates":{"EUR":1,"USD":1.086131,"MXN":17.932246,"SGD":1.462384,"KRW":1460.499318,"THB":39.817943,"TWD":34.789331}}'
        # data = json.loads(rate)
        # return jsonify(data)

        with open(FILE_PATH, "r") as rate:
            data = json.load(rate)   # read this file and convert the content into a Python dictionary
            current_app.logger.debug('Data loaded successfully')
        return jsonify(data)  # Use jsonify to convert the Python dictionary back into JSON format
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404  # Return a 404 error
    except json.JSONDecodeError:
        current_app.logger.error(f"Error in /loaddata: {e}")
        return jsonify({"error": "Invalid JSON data"}), 500  # Return a 500 error
    except IOError as e:
        if not os.path.exists(os.path.dirname(FILE_PATH)): 
            current_app.logger.error('Error: The directory does not exist. {e}')
    except ValueError:
        current_app.logger.error("Error: Incorrect value.")
    except Exception as exception:
        current_app.logger.error(f"Error: An unexpected error occurred: {exception}")


# @main.route("/member")
# @login_required
# def member():     # completed
#     # if 'username' not in session: # user not login yet
#     #     return redirect(url_for("admin.login"))
#     current_app.logger.debug ("Member route accessed")
#     return render_template(
#         "member.html",
#         title="Member",
#         name=current_user.username,
#         # name=session['username'],
#         date=datetime.now()
#     )


# @main.route("/memberNew")
# @login_required
# def member_new():     # completed
#     # if 'username' not in session: # user not login yet
#     #     return redirect(url_for("admin.login"))
#     current_app.logger.debug ("Member route accessed")
#     return render_template(
#         "auth/member_new.html",
#         title="Member",
#         name=current_user.username,
#         # name=session['username'],
#         date=datetime.now()
#     )
