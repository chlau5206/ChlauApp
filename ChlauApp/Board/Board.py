# Board/Board.py -- Contains the routes and CRUD operations

import logging
from flask import render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required 

from .. import db
from .. import csrf
from ..models import  roles_required, handle_exception 
from . import board_bp  
from .BoardModels import Board, BoardForm

ENTRY_LIMIT = 1000    # message limited to 1000
PER_PAGE = 5     # Number of messages per page
logger = logging.getLogger(__name__)

#########################################
# def get_messages(page, per_page=20):
#     return Board.query.order_by(Board.timestamp.desc()) .limit(per_page).offset((page - 1) * per_page).all()

@board_bp.route('/', methods=['GET', 'POST'])     # D = Display
@login_required
def show_message():
    logger.info('Contact Us-Show message route accessed.')
    form = BoardForm()
    
    
    page = request.args.get('page', default=1, type=int)    # Determine the current page number
    
    # Retrieve messages for the current page
    pagination = Board.query.order_by(Board.timestamp.desc()).paginate(page=page, per_page=PER_PAGE)
    message_list = pagination.items

    # Check for next and previous pages
    next_page = pagination.next_num if pagination.has_next else None
    prev_page = pagination.prev_num if pagination.has_prev else None

    # Render the template
    return render_template('board.html', 
                            form=form,
                            messages = message_list, 
                            next_page=next_page, 
                            prev_page=prev_page)


@board_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('sa')  
def delete_message(id):      # R = Remove
    logger.info('message.delete route accessed.')
    
    try: 
        logger.debug(csrf._exempt_views)
        stored_message = Board.query.get_or_404(id)
        if stored_message.name == 'admin' :
            raise ValueError('You cannot delete Admin message.')
        else: 
            db.session.delete(stored_message)
            db.session.commit()
            flash('Message deleted successfully!', 'success')
            logger.warning('Message deleted successfully!')
    except Exception as e:
        error_message = handle_exception(e) 
        flash (f'{error_message}', 'danger')
        logger.error(f'{error_message}')
    
    return redirect(url_for('board_bp.show_message', page=request.args.get('page', 1)))



@board_bp.route('/general_add', methods=['GET', 'POST'])
def general_add_message():
    logger.info('Contact me route accessed')
    
    try:
        current_entries = Board.query.count()  # Get the current number of entries
        if current_entries >= ENTRY_LIMIT:
            raise ValueError('The database has reached its limit of entries. Cannot add more message.')
        
        sform = BoardForm()
        if sform.validate_on_submit():

            new_message = Board(name=sform.name.data.strip(), 
                                email=sform.email.data.strip(),
                                message=sform.message.data.strip()
                                )
            db.session.add(new_message)
            db.session.commit()
            flash('Message added successfully!', 'success')
            logger.warning('New message added')
            # return redirect(url_for('board_bp.general_add_message'))

    except ValueError as error_message:
            flash (f'{error_message}', 'danger')
            logger.error(f'{error_message}')
            # return redirect(url_for('main.home'))
    
    except Exception as e:
            error_message = handle_exception(e) 
            flash (f'{error_message}', 'danger')
            logger.error(f'{error_message}')
            # return redirect(url_for('main.home'))
    finally:
        return render_template('board_general_add.html', form=sform)

