# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template

from .. import db
from . import WebTest1_bp
from .models import TempData


logger = logging.getLogger(__name__)

@WebTest1_bp.route('/')     # D = Display
def index():
    logger.info('WebTest1_Index route accessed.')

    # Add data to the in-memory database
    temp_entry = TempData(data="Temporary info")
    db.session.add(temp_entry)
    db.session.commit()

    # Query data from the in-memory database
    temp_data = TempData.query.all()
    print(temp_data)

    return render_template("index.html", 
                           title="WebTest1 - Index")

