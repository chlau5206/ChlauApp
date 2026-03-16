# about/about2.py -- Contains the routes and CRUD operations


from flask import render_template
# from flask import redirect, url_for, flash, current_app, request
# from flask_login import login_required 

import logging
logger = logging.getLogger(__name__)

from . import about2_bp

@about2_bp.route('/')     
def index():
    logger.debug('about route accessed.')
    return render_template("About21.html", 
                           title="About me (v2)")

