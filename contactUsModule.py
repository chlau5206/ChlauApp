# contact Us Module
## Custom Contact Us #########################

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired

import email_validator 

# ## using CSRF for Contact Us web form #########################
# csrf = CSRFProtect()

class contactForm(FlaskForm): 
    name = StringField(label='Name', validators=[DataRequired()]) 
    email = StringField(label='Email', 
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= StringField(label='Message') 
    submit = SubmitField(label="Submit") 

class loginForm(FlaskForm):
    userName = StringField(label='User name: ', validators=[DataRequired()]) 
    password = PasswordField(label="Password: ", validators=[InputRequired()]) 
    submit = SubmitField(label="Log In") 

class MyForm(FlaskForm): 
    name = StringField('Name', validators=[InputRequired()]) 
    password = PasswordField('Password', validators=[InputRequired()]) 
    # remember_me = BooleanField('Remember me') 
    # salary = DecimalField('Salary', validators=[InputRequired()]) 
    # gender = RadioField('Gender', choices=[ 
    #                     ('male', 'Male'), ('female', 'Female')]) 
    # country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), 
    #                                           ('UK', 'United Kingdom')]) 
    # message = TextAreaField('Message', validators=[InputRequired()]) 
    # photo = FileField('Photo') 

