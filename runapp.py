"""
This script is for the ChlauApp application's entry point. 
"""

''' runapp.py
'''
import sys
import os
from dotenv import load_dotenv
from os import environ
from ChlauApp import app

if __name__ == '__main__':
    ##################################### 
    ## Check Python at lease version 3.10
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
        print("Python 3.10 or higher is required.")
        sys.exit(1)    # fail. 
    else:
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} is running")

    # default Visual Studio settings
    HOST = environ.get('SERVER_HOST' ) 
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        print(f'Error: {ValueError}')
        PORT = 5555
    
    load_dotenv()
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    print (f'host={HOST}; port={PORT}; debug={DEBUG}')    
    app.run(host=HOST, port=PORT, debug=DEBUG)

    # app.run()
    
    

