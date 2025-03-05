# members/__init__.py  

from flask import Blueprint

members_bp = Blueprint('members_bp', __name__, template_folder= 'templates', static_folder='static')

from . import members  # Import routes to register them with the blueprint
