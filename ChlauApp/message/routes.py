# message.py -- contain Contact Us modules
# message module: all CRUD(Create, Read, Update, Delete) operations in one file. 


from flask import render_template, request, redirect, url_for, 
from flask import current_app, Blueprint
from ChlauApp import db, models
from models import Message


message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/')
def show_message():
    message = message.query.all()
    return render_template('message/messages.html', message=message)

@message_bp.route('/add', methods=['POST'])
def add_message():
    name = request.form.get('name')
    course = request.form.get('course')
    grade = request.form.get('grade')
    new_message = message(name=name, course=course, grade=grade)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('message_bp.show_message'))

@message_bp.route('/delete/<int:id>', methods=['POST'])
def delete_message(id):
    message = message.query.get(id)
    if message:
        db.session.delete(message)
        db.session.commit()
    return redirect(url_for('message_bp.show_message'))

@message_bp.route('/update/<int:id>', methods=['POST'])
def update_message(id):
    message = message.query.get(id)
    if message:
        message.name = request.form.get('name')
        message.course = request.form.get('course')
        message.grade = request.form.get('grade')
        db.session.commit()
    return redirect(url_for('message_bp.show_message'))
