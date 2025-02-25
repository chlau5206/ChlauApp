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
    message= TextAreaField(label='Note', 
                        render_kw={'rows': 10, 'cols': 50},
                        validators=[InputRequired(), Length(max=250)])  
    submit = SubmitField(label="Submit") 


# #class ContactUs(db.model):
#     id = db.column(db.integer, primary_key=True)
#     name = db.column(db.string(50), nullable=False)
#     email = db.column(db.string(100), unique=False, nullable=True)
#     message = db.column(db.text, nullable=False)
#     timestamp = db.column(db.datetime, default=datetime.utcnow())

#     def __repr__(self):
#         return f"<message {self.name[:30]} {self.email[:30]} {self.message} {self.timestamp}>"
