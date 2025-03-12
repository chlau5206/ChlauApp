## members/members.py

from os import error
from flask import render_template, redirect, url_for, request, flash, session, current_app
from flask_login import login_required, login_user, logout_user, current_user
from datetime import datetime, timedelta

import os
import shutil
import logging

from .. import db
from .. import login_manager

from . import members_bp

logger = logging.getLogger(__name__)

def get_local_time():
    import pytz

    local_timezone = pytz.timezone('America/Los_Angeles') 
    utc_time = datetime.utcnow()
    local_time = utc_time.astimezone(local_timezone).strftime('%Y-%m-%d %H:%M:%S')

    return local_time

# Set session timeout for each blueprint
@members_bp.before_request
def make_session_permanent():
    session.permanent = True
    session.permanent_session_lifetime = timedelta(minutes=15) # Set session lifetime to 15 min (15 * 60 seconds)

#  Handle session expiration and logout for each blueprint
@members_bp.before_request
def check_session_timeout():
    if 'user_id' in session and session.permanent:
        # Check if the session has expired
        if (datetime.now() - session['last_activity']) > session.permanent_session_lifetime:
            session.pop('user_id', None)
            logout_user()
            return redirect(url_for('auth_bp.login'))
    session['last_activity'] = datetime.now()

@members_bp.route('/')
@members_bp.route('/member')
@login_required
def member():
    user_name = current_user.username
    logger.debug(f'{user_name}, enter member route accessed.')
    
    return render_template(
        "members.html",
        title="Member",
        name=user_name.capitalize(),
        date=get_local_time()
    )


@members_bp.route('/member')
@login_required
def backup_sqlite_db(db_file, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"db_backup_{timestamp}.db")
    shutil.copy2(db_file, backup_file)
    print(f"Database backed up to: {backup_file}")

# if __name__ == "__main__":
#     db_file = "site.db"  # Replace with your database file
#     backup_dir = "backups" # Replace with your backup directory

#     if not os.path.exists(backup_dir):
#         os.makedirs(backup_dir)

#     backup_sqlite_db(db_file, backup_dir)
