# message/__init__.py  

from flask import Blueprint

board_bp = Blueprint('board_bp', __name__)

from . import Board  # Import routes to register them with the blueprint

