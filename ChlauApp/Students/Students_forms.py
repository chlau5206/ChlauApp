from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    submit = SubmitField('Submit')
