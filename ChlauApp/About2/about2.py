# about/about2.py -- Contains the routes and CRUD operations
import os
from flask import render_template , send_from_directory
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

@about2_bp.route("/resume")
def download_resume():
    about2_bp.root_path
    data_folder = os.path.join(about2_bp.root_path, "data")
    return send_from_directory(data_folder, "current_resume.pdf", as_attachment=True)
