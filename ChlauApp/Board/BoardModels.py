''' BoardForm.py 
'''


# from flask import current_app
from flask_wtf import FlaskForm #, CSRFProtect
from wtforms import StringField,  TextAreaField, SubmitField #, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired, Length

#import sqlalchemy
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text
from sqlalchemy.sql import func

from .. import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True) 
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime,
                          default=func.current_timestamp(),
                          onupdate=func.current_timestamp())  # Add onupdate parameter) # Add the timestamp column

    def __repr__(self):
        return f"<message {self.name[:30]} {self.email[:30]} {self.message} {self.timestamp}>"

class BoardForm(FlaskForm): 
    name = StringField(label='Name', render_kw={'maxlength': 80, 'size': 30, 'style': 'width:300px;'},
                      validators=[InputRequired()]) 
    email = StringField(label='Email', render_kw={'maxlength': 120, 'size': 30, 'style': 'width:300px;'},
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= TextAreaField(label='Note', render_kw={'rows': 40, 'cols': 60},
                        validators=[InputRequired(), Length(max=240)])  
    submit = SubmitField(label="Submit") 

