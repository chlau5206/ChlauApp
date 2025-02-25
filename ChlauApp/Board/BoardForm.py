''' BoardForm.py 
'''

# from flask import current_app
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class BoardForm(FlaskForm): 
    name = StringField(label='Name', render_kw={'maxlength': 50, 'size': 30, 'style': 'width:300px;'},
                      validators=[InputRequired()]) 
    email = StringField(label='Email', render_kw={'maxlength': 50, 'size': 30, 'style': 'width:300px;'},
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= TextAreaField(label='Note', render_kw={'rows': 10, 'cols': 50},
                        validators=[InputRequired(), Length(max=250)])  
    submit = SubmitField(label="Submit") 


