''' Flask web page -- views.py
'''
# from . import main
from flask import render_template, session, redirect, url_for, flash
#, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_login import current_user, login_required
from datetime import datetime


from .models import Message
from . import db
from . import FormModule   # contactUsModule import contactForm
from . import admin

#  create Blueprint
from flask import Blueprint
main = Blueprint('main', __name__)


##############
# Main Route #
##############

@main.route("/")
@main.route("/home/")
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

@main.route("/member")
@login_required
def member():
    # if 'username' not in session: # user not login yet
    #     return redirect(url_for("admin.login"))
    print ("** member route **")
    return render_template(
        "member.html",
        name=current_user.username,
        # name=session['username'],
        date=datetime.now()
    )
    

