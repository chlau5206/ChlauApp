## Custom Contact Us #########################
# from . import app
# from flask import Flask, render_template, request, redirect, url_for 
# import email_validator 

from flask_wtf import FlaskForm 
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email 
  
class contactForm(FlaskForm): 
    name = StringField(label='Name', validators=[DataRequired()]) 
    email = StringField(label='Email', validators=[ 
        DataRequired(), Email(granular_message=True)]) 
    message= StringField(label='Message') 
    submit = SubmitField(label="Log In") 
