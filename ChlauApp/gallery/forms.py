""" apps/gallery/forms.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    photo = FileField('Upload Photo', validators=[DataRequired()])
    library = SelectField('Select Library', coerce=int, validators=[DataRequired()])
    title = StringField('Title')
    description = TextAreaField('Description')
    submit = SubmitField('Upload')

    def __init__(self, libraries, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.library.choices = [(lib.id, lib.name) for lib in libraries]

class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
