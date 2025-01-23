# contact Us Module
## Custom Contact Us #########################

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired

# from . import app
# import email_validator 
# ## using CSRF for Contact Us web form #########################
# csrf = CSRFProtect(app)

class contactForm(FlaskForm): 
    name = StringField(label='Name', validators=[InputRequired()]) 
    email = StringField(label='Email', 
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= StringField(label='Message') 
    submit = SubmitField(label="Submit") 

class LoginForm(FlaskForm):
    username = StringField(label='Username: ', validators=[InputRequired()]) 
    password = PasswordField(label="Password: ", validators=[InputRequired()]) 
    submit = SubmitField(label="Login") 

