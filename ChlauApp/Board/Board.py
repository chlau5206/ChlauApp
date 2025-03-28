# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required 

from .. import db
from ..models import  roles_required, handle_exception 
from . import board_bp  
from .BoardModels import Board, BoardForm

ENTRY_LIMIT = 1000    # message limited to 1000
logger = logging.getLogger(__name__)

#########################################
def get_messages(page, per_page=20):
    return Board.query.order_by(Board.timestamp.desc()) .limit(per_page).offset((page - 1) * per_page).all()

@board_bp.route('/')     # D = Display
@login_required
def show_message():
    logger.debug('Contact Us-Show message route accessed.')
    form = BoardForm()
    page = form.page.data if form.validate_on_submit() else request.args.get('page', 1, type=int)
    message_list = Board.query.order_by(Board.timestamp.desc()) \
        .limit(20).offset((page - 1) * 20).all()
    next_page = page + 1
    prev_page = page - 1 if page > 1 else None
    return render_template('board.html', 
                            form=form,
                            messages = message_list, 
                            next_page=next_page, 
                            prev_page=prev_page)

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


"""
@board_bp.route('/addMsgs')    
@login_required
def populate_messages():
    logger.debug('Populate message route accessed.')
    msg = dict()
    
    msg["askd"] = {"email": "fasd@kjakj.com", "message": "234f"}
    msg["fjfg"] = {"email": "sd@kjj.fgfgfc", "message": "5656"}
    msg["fgfjfyt"] = {"email": "sftyfyd@kjjjjakj.klkc", "message": "688"}
    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["gdtydy"] = {"email": "s77d@kjakj.c", "message": "955"}
    
    msg["fgfjfyt"] = {"email": "sftyfyd@kjjjjakj.klkc", "message": "688"}
    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["askd"] = {"email": "fasd@kjakj.com", "message": "234f"}
    msg["fjfg"] = {"email": "sd@kjj.fgfgfc", "message": "5656"}
    msg["gdtydy"] = {"email": "s77d@kjakj.c", "message": "955"}

    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["askd"] = {"email": "fasd@kjakj.com", "message": "234f"}
    msg["fjfg"] = {"email": "sd@kjj.fgfgfc", "message": "5656"}
    msg["fgfjfyt"] = {"email": "sftyfyd@kjjjjakj.klkc", "message": "688"}
    msg["fgf23342jfyt"] = {"email": "sft2yd@kjjjjakj.klkc", "message": "68228"}
    
    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["gdtydy"] = {"email": "s77d@kjakj.c", "message": "955"}
    msg["askd"] = {"email": "fasd@kjakj.com", "message": "234f"}
    msg["fjfg"] = {"email": "sd@kjj.fgfgfc", "message": "5656"}
    msg["fjfg"] = {"email": "sd@kjj.fgfgfc", "message": "5656"}
    
    msg["askd"] = {"email": "fasd@kjakj.com", "message": "234f"}
    msg["fgfjfyt"] = {"email": "sftyfyd@kjjjjakj.klkc", "message": "688"}
    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["ffg"] = {"email": "sjjd@kjjjakj.jhc", "message": "89"}
    msg["gdtydy"] = {"email": "s77d@kjakj.c", "message": "955"}


    for key, value in msg.items():
        # for key, value in value.items():
            # new_message = Board(name=key,
            #                     email=value[email],
            #                     message=value[message])

        pass
        db.session.add(new_message)
        db.session.commit()



@board_bp.route('/feedbacks')
def feedbacks():
    page = request.args.get('page', 1, type=int)
    feedback_list = get_feedbacks(page)
    next_page = page + 1
    prev_page = page - 1 if page > 1 else None
    
    return render_template('feedback_list.html', feedbacks=feedback_list, next_page=next_page, prev_page=prev_page)

<div class="container">
  <h1 class="title">User Feedback</h1>
  <div class="feedback-list">
    {% for feedback in feedbacks %}
      <div class="box">
        <p>{{ feedback.message }}</p>
        <p><small>{{ feedback.created_at }}</small></p>
      </div>
    {% endfor %}
  </div>
  <nav class="pagination" role="navigation" aria-label="pagination">
    {% if prev_page %}
      <a class="pagination-previous" href="{{ url_for('feedback.feedbacks', page=prev_page) }}">Previous</a>
    {% endif %}
    <a class="pagination-next" href="{{ url_for('feedback.feedbacks', page=next_page) }}">Next</a>
  </nav>
</div>
"""

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