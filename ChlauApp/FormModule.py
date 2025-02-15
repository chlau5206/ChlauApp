# contact Us Module
## Custom Contact Us #########################

from flask import current_app
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired

# import email_validator 

class contactForm(FlaskForm): 
    name = StringField(label='Name', render_kw={'maxlength': 50, 'size': 30, 'style': 'width:300px;'},
                      validators=[InputRequired()]) 
    email = StringField(label='Email', render_kw={'maxlength': 50, 'size': 30, 'style': 'width:300px;'},
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= TextAreaField(label='Message', render_kw={'rows': 10, 'cols': 50},
                         validators=[InputRequired()])  
    submit = SubmitField(label="Submit") 

class LoginForm(FlaskForm):
    username = StringField(label='Username: ', validators=[InputRequired()]) 
    password = PasswordField(label='Password: ', validators=[InputRequired()]) 
    submit = SubmitField(label="Login") 

