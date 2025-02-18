# # models.py

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
# from ChlauApp import db
from . import db

class User(UserMixin, db.Model):
    # from flask_login import UserMixin
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(10), nullable=False)    # Add role field
    # email = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role}', password='{self.password}')>"
        

# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(250), unique=False, nullable=True)
#     message = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow())

#     def __repr__(self):
#         return f"<Message {self.name[:30]} {self.message} {self.timestamp}>"




