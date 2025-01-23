# contact Us Module
## Custom Contact Us #########################

# from flash import Flask, render_template, request, flash
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
    username = StringField(label='User name: ', validators=[InputRequired()]) 
    password = PasswordField(label="Password: ", validators=[InputRequired()]) 
    submit = SubmitField(label="Login") 

# class MyForm(FlaskForm): 
#     name = StringField('Name', validators=[InputRequired()]) 
#     password = PasswordField('Password', validators=[InputRequired()]) 
    # remember_me = BooleanField('Remember me') 
    # salary = DecimalField('Salary', validators=[InputRequired()]) 
    # gender = RadioField('Gender', choices=[ 
    #                     ('male', 'Male'), ('female', 'Female')]) 
    # country = SelectField('Country', choices=[('IN', 'India'), ('US', 'United States'), 
    #                                           ('UK', 'United Kingdom')]) 
    # message = TextAreaField('Message', validators=[InputRequired()]) 
    # photo = FileField('Photo') 

