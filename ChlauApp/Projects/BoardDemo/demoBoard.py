# Board/BoardDemo.py -- Contains the routes and CRUD operations


from flask import render_template, redirect, url_for, flash, current_app, request
from flask_login import login_required 

from . import boardDemo_bp  
from ...extensions import db, csrf
from ...utils.utilities import handle_SQL_exception
from .BoardDemoModels import BoardDemoTbl, BoardDemoForm

import logging
logger = logging.getLogger(__name__)

ENTRY_LIMIT = 50    # message limited to 50
PER_PAGE = 5        # Number of messages per page

#########################################
# def get_messages(page, per_page=10):
#     return BoardDemo.query.order_by(BoardDemo.timestamp.desc()) .limit(per_page).offset((page - 1) * per_page).all()

# Operation: Create
@boardDemo_bp.route('/Demo_add', methods=['GET', 'POST'])
@login_required
def demo_add_message():                     
    logger.info('Contact me route accessed')
    
    sform = BoardDemoForm()
    try:
        current_entries = BoardDemoTbl.query.count()  # Get the current number of entries
        if current_entries >= ENTRY_LIMIT:
            raise ValueError('The database has reached its limit of entries.')
        
        
        if sform.validate_on_submit():
            new_message = BoardDemoTbl(name=sform.name.data.strip(), 
                                email=sform.email.data.strip(),
                                message=sform.message.data.strip()
                                )
            db.session.add(new_message)
            db.session.commit()
            flash('Message added successfully!', 'success')
            logger.warning('New message added')
            # return redirect(url_for('boardDemo_bp.demo_add_message'))

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
        return render_template('boardDemo_add.html', form=sform)


# Operation: Display
@boardDemo_bp.route('/', methods=['GET', 'POST'])     # D = Display
@login_required
def demo_show_message():
    logger.info('Contact Us-Show message route accessed.')
    sform = BoardDemoForm()
    page = request.args.get('page', default=1, type=int)    # Determine the current page number
    
    # Retrieve messages for the current page
    pagination = BoardDemoTbl.query.order_by(BoardDemoTbl.timestamp.desc()).paginate(page=page, per_page=PER_PAGE)
    message_list = pagination.items

    # Check for next and previous pages
    next_page = pagination.next_num if pagination.has_next else None
    prev_page = pagination.prev_num if pagination.has_prev else None

    # Render the template
    return render_template('boardDemo.html', 
                            form=sform,
                            messages = message_list, 
                            next_page=next_page, 
                            prev_page=prev_page)

# Operation: Delete
@boardDemo_bp.route('/DemoDelete/<int:id>', methods=['POST'])
@login_required
# @roles_required('sa')  
def demo_delete_message(id):      # R = Remove
    logger.info('message.delete route accessed.')
    
    try: 
        logger.debug(csrf._exempt_views)
        stored_message = BoardDemoTbl.query.get_or_404(id)
        # if stored_message.name == 'admin' :
        #     raise ValueError('You cannot delete Admin message.')
        # else: 
            
        db.session.delete(stored_message)
        db.session.commit()
        flash('Message deleted successfully!', 'success')
        logger.warning('Message deleted successfully!')
    except Exception as e:
        error_message = handle_SQL_exception(e) 
        flash (f'{error_message}', 'danger')
        logger.error(f'{error_message}')
    
    return redirect(url_for('boardDemo_bp.show_message', page=request.args.get('page', 1)))

