""" apps/gallery/__init__.py
"""
from flask import Blueprint , current_app

import os

basedir = os.path.abspath(os.path.dirname(__file__))
gallery_bp = Blueprint('gallery', __name__, template_folder='templates', static_folder='static')

# Configuration settings
UPLOAD_FOLDER = os.path.join(gallery_bp.static_folder, 'uploads')

# Assuming app is already created and imported
def configure_gallery(app):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    from . import models
    with app.app_context():
        models.populate_libraries()

from . import views
