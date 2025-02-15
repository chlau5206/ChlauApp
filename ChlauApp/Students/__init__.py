# Students/__init__.py  

from flask import Blueprint

students_bp = Blueprint('students_bp', __name__)

from . import Students  # Import routes to register them with the blueprint

