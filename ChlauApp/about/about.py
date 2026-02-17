# about/about.py -- Contains the routes and CRUD operations


from flask import render_template
from . import about_bp

import logging
logger = logging.getLogger(__name__)

@about_bp.route('/')     
def index():
    logger.debug('about route accessed.')
    return render_template("about.html", 
                           title="About me")

