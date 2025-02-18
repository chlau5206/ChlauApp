''' Students_forms.py 
'''
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = SelectField('Courses', choices=[
        ('eng', 'English'), 
        ('art', 'Art'), 
        ('mus', 'Music'),
        ('bus','Business'),
        ('phy', 'Physic'), 
        ('his', 'History')
        ], validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    submit = SubmitField('Submit')
