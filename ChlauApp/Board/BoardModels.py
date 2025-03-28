''' Board/BoardForm.py 
'''
from doctest import script_from_examples
from .. import db
from sqlalchemy import Text, Index, desc
from sqlalchemy.sql import func

from flask_wtf import FlaskForm #, CSRFProtect
from wtforms import StringField,  TextAreaField, SubmitField, IntegerField #, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired, Length


class Board(db.Model):
    __tablename__ = 'Board'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=True) 
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime,
                          default=func.current_timestamp(),   # Add current timestamp when created
                          onupdate=func.current_timestamp())  # Add onupdate parameter 
     # Add an index for the timestamp column in descending order
    __table_args__ = (
        Index('ix_Board_timestamp_desc', desc(timestamp)),    
        )

    def __repr__(self):
        return f"<message {self.name[:30]} {self.email[:30]} {self.message} {self.timestamp}>"

class BoardForm(FlaskForm): 
    name = StringField(label='Name', render_kw={'maxlength': 80, 'size': 30, 'style': 'width:300px;'},
                      validators=[InputRequired()]) 
    email = StringField(label='Email', render_kw={'maxlength': 120, 'size': 30, 'style': 'width:300px;'},
                        validators=[DataRequired(), Email(granular_message=True)]) 
    message= TextAreaField(label='Note', render_kw={'rows': 40, 'cols': 60},
                        validators=[InputRequired(), Length(max=240)])  
    page = IntegerField('Page', default=1)  # For pagination
    submit = SubmitField(label="Send") 

"""
1. Generate a Migration If you're using Flask-Migrate, generate a migration file to apply the index to your database:
    Bash
    flask db migrate -m "Add descending index to timestamp column"

2. Migration script
    Python 
    from alembic import op
    import sqlalchemy as sa

    def upgrade():
        op.create_index('ix_feedback_created_at_desc', 'feedback', ['created_at'], unique=False)

    def downgrade():
        op.drop_index('ix_feedback_created_at_desc', table_name='feedback')

3. Apply the Migration 
    Bash
    flask db upgrade

"""
