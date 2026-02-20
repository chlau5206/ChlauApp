# about/about.py -- Contains the routes and CRUD operations


from flask import render_template
from flask import redirect, url_for, flash, current_app, request
from flask_login import login_required 

import logging
logger = logging.getLogger(__name__)

from . import home2_bp


@home2_bp.route('/')     
def index():
    logger.debug('Home route accessed.')
    return render_template("home2.html", 
                           title="Home (v2)")

