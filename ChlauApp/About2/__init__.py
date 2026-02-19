# Board/__init__.py  

from flask import Blueprint

about2_bp = Blueprint('about2_bp', __name__, template_folder= 'templates', static_folder='static')

from . import about2  # Import routes to register them with the blueprint

