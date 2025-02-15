# message.py -- contain Contact Us modules
# message module: all CRUD(Create, Read, Update, Delete) operations in one file. 


from flask import render_template, request, redirect, url_for, 
from flask import current_app
from ChlauApp import db, models
from models import Message

from flask import Blueprint
message = Blueprint('message', __name__)

@message.route('/')
def show_message():
    message = message.query.all()
    return render_template('message/messages.html', message=message)

@message.route('/add', methods=['POST'])
def add_message():
    name = request.form.get('name')
    course = request.form.get('course')
    grade = request.form.get('grade')
    new_message = message(name=name, course=course, grade=grade)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('message.show_message'))

@message.route('/delete/<int:id>', methods=['POST'])
def delete_message(id):
    message = message.query.get(id)
    if message:
        db.session.delete(message)
        db.session.commit()
    return redirect(url_for('message.show_message'))

@message.route('/update/<int:id>', methods=['POST'])
def update_message(id):
    message = message.query.get(id)
    if message:
        message.name = request.form.get('name')
        message.course = request.form.get('course')
        message.grade = request.form.get('grade')
        db.session.commit()
    return redirect(url_for('message.show_message'))
