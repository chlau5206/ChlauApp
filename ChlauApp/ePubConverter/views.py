# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template
from . import ePubConv_bp

logger = logging.getLogger(__name__)

@ePubConv_bp.route('/')     
def index():
    logger.debug('ePubConverter route accessed.')
    return render_template("ePubConverter.html", 
                           title="ePub Converter")

