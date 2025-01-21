# # models.py

from . import db
# from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    # from flask_login import UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
