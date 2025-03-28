''' app1/forms.py
'''
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired, InputRequired

class AuthForm(FlaskForm):
    username = StringField(label='Username: ', validators=[InputRequired()]) 
    password = PasswordField(label='Password: ', validators=[InputRequired()]) 
    role = SelectField('Role',
                         choices=[
                             ('member', 'Member'), 
                             ('guest', 'Guest'),
                             ('dev','Dev'),
                             ('sa', 'SA')
                             ],
                                
                         validators=[DataRequired()]
                         )
    submit = SubmitField(label="Submit") 



