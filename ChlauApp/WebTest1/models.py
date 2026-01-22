''' test1/models.py
'''

import logging
from . import db
# from . import WebTest1_bp
from flask import redirect, url_for, flash, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from sqlalchemy import CheckConstraint, Text, Index, desc
from sqlalchemy.sql import func
from sqlalchemy.exc import  SQLAlchemyError, IntegrityError, OperationalError,ProgrammingError,DataError, InternalError
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired

from flask_login import UserMixin, current_user
from werkzeug.exceptions import HTTPException
from datetime import datetime
from functools import wraps


class TempData(db.Model):  # This model will use the in-memory database
    __tablename__ = 'WebTest1'
    __bind_key__ = 'memory'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime,
                          default=func.current_timestamp(),   # Add current timestamp when created
                          onupdate=func.current_timestamp())  # Add onupdate parameter 
     # Add an index for the timestamp column in descending order
    __table_args__ = (
        Index('ix_Board_timestamp_desc', desc(timestamp)),    
        )

    def __repr__(self):
        # Handle attributes safely with default values and slicing
        data = (self.data[:120] if self.data else "N/A")
        return f"<data {self.timestamp}: {data}>"

# class Sample_Form(FlaskForm): 
#     name = StringField(label='Name', render_kw={'maxlength': 80, 'size': 30, 'style': 'width:300px;'},
#                       validators=[InputRequired()]) 
#     email = StringField(label='Email', render_kw={'maxlength': 120, 'size': 30, 'style': 'width:300px;'},
#                         validators=[DataRequired(), Email(granular_message=True)]) 
#     message= TextAreaField(label='Note', render_kw={'rows': 40, 'cols': 60},
#                         validators=[InputRequired(), Length(max=240)])  
#     page = IntegerField('Page', default=1)  # For pagination
#     submit = SubmitField(label="Send") 

