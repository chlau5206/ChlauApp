# # models.py

from flask import current_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ChlauApp import db

class User(UserMixin, db.Model):
    # from flask_login import UserMixin
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # email = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(250), unique=False, nullable=True)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Message {self.name[:30]} {self.message} {self.timestamp}>"

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(10), nullable=False)




