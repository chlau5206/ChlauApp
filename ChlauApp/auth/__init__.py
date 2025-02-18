# auth/__init__.py  

from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)

from . import auth  # Import routes to register them with the blueprint

