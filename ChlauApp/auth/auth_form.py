''' auth_forms.py 
'''
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired

class AuthForm(FlaskForm):
    username = StringField(label='Username: ', validators=[InputRequired()]) 
    password = PasswordField(label='Password: ', validators=[InputRequired()]) 
    options = SelectField('Role',
                         choices=[
                             ('sa', 'SA'),
                             ('member', 'Member'), 
                             ('guest', 'Guest')],
                         validators=[DataRequired()]
                         )
    submit = SubmitField(label="Submit") 

