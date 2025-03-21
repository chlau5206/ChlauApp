# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template
from . import about_bp

logger = logging.getLogger(__name__)

@about_bp.route('/')     # D = Display
def index():
    logger.debug('about route accessed.')
    return render_template("index.html", 
                           title="About me")

