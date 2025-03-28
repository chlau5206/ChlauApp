''' app1/models.py
'''

from flask import current_app
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired

# import email_validator 

class Sample(FlaskForm):
    username = StringField(label='Username: ', validators=[InputRequired()]) 
    password = PasswordField(label='Password: ', validators=[InputRequired()]) 
    submit = SubmitField(label="Login") 


