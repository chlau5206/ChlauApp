# home2/__init__.py  

from flask import Blueprint

home2_bp = Blueprint('home2_bp', __name__, template_folder= 'templates', static_folder='static')

from . import home2  # Import routes to register them with the blueprint

