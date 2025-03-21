# Board/__init__.py  

from flask import Blueprint

about_bp = Blueprint('about_bp', __name__, template_folder= 'templates', static_folder='static')

from . import views  # Import routes to register them with the blueprint

