# Contact_Us/Contact_Us.py -- Contains the routes and CRUD operations

from os import error
from venv import logger
from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_required, current_user
#from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, OperationalError
from email.policy import default
from mailbox import Message
from smtplib import SMTPException

from .. import db
from .. import login_manager
from .. import mail
from ..models import Board, roles_required, get_local_time
from . import board_bp  # Contact_Us_bp blueprint
from .BoardForm import BoardForm

ENTRY_LIMIT = 200

''' class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    course_name = lambda x : course_code[x]
    course_code = {
        'eng': 'English', 
        'art': 'Art',
        'mus': 'Music', 
        'bus': 'Business',
        'phy': 'Physic',
        'his': 'History'
                   }

    def __repr__(self):
         return f"<Message(name='{self.name}', course='{self.course}', grade='{self.grade}')>"

    def table_exists(table_name):
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        return inspector.has_table(table_name)

    @student_bp.before_app_first_request
    # logger.error('before_app_first_request method not found.')
    def startup_check():
        import os
        if not table_exists('Message'):
            current_app.logger.error("Table 'Message' does not exist. Creating table.")
            db.create_all()  # This will create all tables defined by the models
        else:
            current_app.logger.debug("Table 'Message' exists.")

    from functools import wraps
    def roles_required(*roles):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                if current_user.role not in roles:
                    flash('You do not have permission to access this page.', 'danger')
                    return redirect(url_for('message_bp.show_message'))
                return f(*args, **kwargs)
            return decorated_function
        return decorator

    @Student_bp.route('/add', methods=['GET', 'POST'])
    @login_required
    @roles_required('teacher', 'TA')  # Allow both teachers and TAs to add message
    def add_Message():
        form = MessageForm()

        return render_template('message/add_Message.html', form=form)


'''


@board_bp.route('/')     # D = Display
@login_required
def show_message():
    logger.debug('Contact Us-Show message route accessed.')
    form = BoardForm()
    messages = Board.query.all()
    return render_template('Board/board.html', messages=messages, form=form)

@board_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_message():           # C = Create
    current_app.logger.debug('Board-add route accessed')
    current_entries = Board.query.count()  # Get the current number of entries
    
    if current_entries >= ENTRY_LIMIT:
        flash('The database has reached its limit of entries. Cannot add more message.', 'danger')
        return redirect(url_for('board_bp.show_message'))

    sform = BoardForm()
    if sform.validate_on_submit():
        new_message = Board(name=sform.name.data, 
                                email=sform.email.data,
                                message=sform.message.data)
        db.session.add(new_message)
        db.session.commit()
        flash('Message added successfully!', 'success')
        return redirect(url_for('board_bp.show_message'))
    return render_template('Board/board_add.html', form=sform)

@board_bp.route('/general_add', methods=['GET', 'POST'])
def general_add_message():
    current_app.logger.debug('board_bp-general add route accessed')
    current_entries = Board.query.count()  # Get the current number of entries

    if current_entries >= ENTRY_LIMIT:
        flash('The database has reached its limit of entries. Cannot add more message.', 'danger')
        return redirect(url_for('main.home'))

    sform = BoardForm()
    if sform.validate_on_submit():
        new_message = Board(name=sform.name.data, 
                                email=sform.email.data,
                                message=sform.message.data)
        db.session.add(new_message)
        db.session.commit()
        flash('Message added successfully!', 'success')
        return redirect(url_for('board_bp.general_add_message'))
    return render_template('Board/board_general_add.html', form=sform)

@board_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_message(id):       # U = Update
    current_app.logger.debug ('message-update route accessed.')
    stored_message = Board.query.get_or_404(id)
    form = BoardForm(obj=Message)
    if form.validate_on_submit():
        stored_message.name = form.name.data
        stored_message.email = form.email.data
        stored_message.message = form.message.data
        db.session.commit()
        flash('Message updated successfully!', 'success')
        return redirect(url_for('board_bp.show_message'))
    return render_template('Board/board_update.html', form=form, Message=stored_message)

@board_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_message(id):      # R = Remove
    current_app.logger.debug('message.delete route accessed.')
    stored_message = Board.query.get_or_404(id)
    db.session.delete(stored_message)
    db.session.commit()
    flash('Message deleted successfully!', 'success')
    return redirect(url_for('board_bp.show_message'))

# def send_email(Message):
#     current_app.logger.debug('message-mail route access.')
#     msg = Message('New Message Added',
#                   sender='your_email@gmail.com',
#                   recipients=['recipient@example.com'])
#     msg.body = f'Name: {Message.name}\nCourse: {Message.course}\nGrade: {Message.grade}'
#     mail.send(msg)
