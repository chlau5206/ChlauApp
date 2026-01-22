# Board/__init__.py  

from flask import Blueprint

WebTest1_bp = Blueprint('WebTest1_bp', __name__, template_folder= 'templates', static_folder='static')

from . import views  # Import routes to register them with the blueprint

