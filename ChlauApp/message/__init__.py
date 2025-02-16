# __init__.py for ChlauApp.message 

from flask import Blueprint

message_bp = Blueprint('message_bp', __name__)

from . import message  # Import routes to register them with the blueprint
