""" apps/gallery/models.py
"""

from .. import db
from datetime import datetime

class Library(db.Model):
    __tablename__ = 'libraries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    photos = db.relationship('Photo', backref='photos_library', lazy=True)

    def __repr__(self):
        return f'<Library {self.name}>'

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'), nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Photo {self.filename}>'

def populate_libraries():
    initial_libraries = ["Nature", "Travel", "Pets", "Family", "Abstract"] # List of libraries

    for lib_name in initial_libraries:
        if not Library.query.filter_by(name=lib_name).first():
            new_lib = Library(name=lib_name)
            db.session.add(new_lib)
    db.session.commit()