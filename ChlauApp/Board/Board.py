# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template, redirect, url_for, flash, current_app
from flask_login import login_required 
from .. import db
from ..models import  roles_required, handle_exception 
from . import board_bp  
from .BoardModels import Board, BoardForm

ENTRY_LIMIT = 200    # message limited to 200
logger = logging.getLogger(__name__)

@board_bp.route('/')     # D = Display
@login_required
def show_message():
    logger.debug('Contact Us-Show message route accessed.')
    form = BoardForm()
    messages = Board.query.order_by(Board.timestamp.desc()).all()
    return render_template('board.html', messages=messages, form=form)

@board_bp.route('/general_add', methods=['GET', 'POST'])
def general_add_message():
    current_app.logger.debug('board_bp-general add route accessed')
    
    try:
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

    except Exception as e:
            error_message = handle_exception(e) 
            flash (f'{error_message}', 'error')
            logger.error(f'{error_message}')

    return render_template('board_general_add.html', form=sform)

@board_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('sa', 'member')  # Only admins can register new users
def reply_message(id):       # U = Update
    current_app.logger.debug ('message-reply route accessed.')
    stored_message = Board.query.get_or_404(id)
    sform = BoardForm(obj=stored_message)

    try: 
        current_entries = Board.query.count()  # Get the current number of entries
    
        if current_entries >= ENTRY_LIMIT:
            flash('The database has reached its limit of entries. Cannot add more message.', 'danger')
            logger.error('The database has reached its limit of entries. Cannot add more message.')
            return redirect(url_for('board_bp.show_message'))

        if sform.validate_on_submit():
            replied_message = Board(name=sform.name.data, 
                                    email=sform.email.data,
                                    message=sform.message.data)
            db.session.add(replied_message)
            db.session.commit()
            flash(f'client={sform.name.data} message replied!', 'success')
            logger.info(f'client={sform.name.data} message replied!')
            return redirect(url_for('board_bp.show_message'))

    except Exception as e:
            error_message = handle_exception(e) 
            flash (f'{error_message}', 'error')
            logger.error(f'{error_message}')

    return render_template('board_reply.html', form=sform, message=stored_message)

@board_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_message(id):      # R = Remove
    current_app.logger.debug('message.delete route accessed.')
    
    try: 
        stored_message = Board.query.get_or_404(id)
        if stored_message.name == 'Admin' :
            raise ValueError('You cannot delete Admin message.')
        else: 
            db.session.delete(stored_message)
            db.session.commit()
            flash('Message deleted successfully!', 'success')
            logger.debug('Message deleted successfully!')
    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'{error_message}', 'error')
        logger.error(f'{error_message}')
    
    return redirect(url_for('board_bp.show_message'))


""" send email feature not implemented.  Did not support basic auth in both MS and google.
    Must use oAuth for auth.

def send_email(message):
    current_app.logger.debug('message-mail route access.')
    msg = Message(subject='New Message Added',
                  sender='your_email@gmail.com',
                  recipients=['recipient@example.com']
                  body=message
                  )
    try:
        mail.send(msg)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {e}', 'danger')

"""