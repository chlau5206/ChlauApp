# Board/Board.py -- Contains the routes for add message operations

from flask import render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required 

from . import board_bp  
from ..extensions import db, csrf
from ..AppAdmin.members.models import handle_SQL_exception
from ..AppAdmin.adminBoard.BoardModels import Board, BoardForm

import logging
logger = logging.getLogger(__name__)

ENTRY_LIMIT = 50   # message limited to 50
PER_PAGE = 5     # Number of messages per page

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
            error_message = handle_SQL_exception(e) 
            flash (f'{error_message}', 'danger')
            logger.error(f'{error_message}')
            # return redirect(url_for('main.home'))
    finally:
        return render_template('board_general_add.html', form=sform)


