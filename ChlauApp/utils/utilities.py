# main/errors.py

# from sqlalchemy import CheckConstraint #, Text, Index, desc
# from sqlalchemy.sql import func

from sqlalchemy.exc import  SQLAlchemyError, IntegrityError, OperationalError,ProgrammingError,DataError, InternalError
from werkzeug.exceptions import HTTPException

import logging
logger = logging.getLogger(__name__)


def handle_SQL_exception(e):  # first version
    SQLERROR = (SQLAlchemyError, IntegrityError, OperationalError, 
            ProgrammingError, DataError,InternalError)

    if isinstance(e, IOError):
        return "I/O exception: {}".format(e)
    # elif isinstance(e, smtplib.SMTPException):
    #     return "SMTP exception: {}".format(e.strerror)
    elif isinstance(e, SQLERROR):
        db.session.rollback()
        logger.warning('database session rollbacked.')
        return "SQL exception: {}".format(e)
    elif isinstance(e,HTTPException ):
        error_message = f'HTTP Exception:{e.code}:{e.name}:{e.description}'
        return error_message
    else:
        logger.error(f'UnexpectedError: {e}')
        return "An unexpected exception: {}".format(e)