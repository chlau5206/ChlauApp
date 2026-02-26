# BoardDemo/__init__.py  

from flask import Blueprint

boardDemo_bp = Blueprint('boardDemo_bp', __name__, template_folder= 'templates', static_folder='static')

from . import routes_boardDemo  # Import routes to register them with the blueprint
