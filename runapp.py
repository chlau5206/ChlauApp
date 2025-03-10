"""
This script is for the ChlauApp application's entry point. 
"""

''' runapp.py
'''
import os, sys
from ChlauApp import app

if __name__ == '__main__':
    
    #####################################
    ## Check Python at lease version 3.10
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} is running")
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
        print("*** Python 3.10 or higher is required ***")
        sys.exit(1)    # if fail. 

    # print(f"Template folder:  {app.jinja_env.loader.searchpath}")
    # print(f"Static folder:    {app.static_folder}")

    if app.config['FLASK_ENV'] == 'development':
        DEBUG = app.config['DEBUG'] == True
        HOST = os.environ.get('SERVER_HOST', 'localhost')
        try:
            PORT = int(os.environ.get('SERVER_PORT', '5555'))
        except ValueError:
            PORT = 5555
        app.run(HOST, PORT, debug=DEBUG)
    else: 
        app.run()
