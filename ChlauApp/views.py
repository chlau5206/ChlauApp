''' Flask web page -- views.py
'''
# from . import main
from flask import render_template, session, redirect, url_for, flash
from flask import Flask,request, json, jsonify, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import current_user, login_required
from datetime import datetime

from .models import Message
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
    # users = models.User.query.all()
    return render_template("home.html")
main.add_url_rule('/', 'home', home)

@main.route("/about/")
def about():     # completed
    return render_template("about.html")

@main.route("/contact/", methods=["GET", "POST"])
def contact():   # bug: message no show.
    cform = FormModule.contactForm()

    if cform.validate_on_submit():
        new_message = Message(message=cform.message.data)
        try:
            db.session.add(new_message)
            db.session.commit()
            print ('Message and user saved!')
            return redirect(url_for('home'))
        except:
            print ('There was an issue saving your message.')
        return redirect(url_for('main.home'))
    else:
        print('not on submitted.')

    return render_template("contact.html", form=cform)

@main.route("/exchangeRate/")
def exchangeRate():   
    return render_template("exchangeRate.html")

@main.route("/loadExchangeRate")
def load_exchange_rate():
    FILE_PATH = os.path.join(main.root_path, 'static', 'data', 'latestRate.json')
    # r"ChlauApp/static/data/latestRate.json"
    try:
        with open(FILE_PATH, "r") as rate:
            data = json.load(rate)
            return jsonify(data)  # Use jsonify to return JSON data
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404  # Return a 404 error
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON data"}), 500  # Return a 500 error
    except IOError as e: 
        if not os.path.exists(os.path.dirname(FILE_PATH)): 
            print (f"Error: The directory does not exist. {FILE_PATH}")
    except ValueError:
        print ("Error: Incorrect value.")
    except Exception as e:
        print (f"Error: An unexpected error occurred: {e}")
            

@main.route("/member")
@login_required
def member():     # completed
    # if 'username' not in session: # user not login yet
    #     return redirect(url_for("admin.login"))
    print ("** member route **")
    return render_template(
        "member.html",
        name=current_user.username,
        # name=session['username'],
        date=datetime.now()
    )
    

