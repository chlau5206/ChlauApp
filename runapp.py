"""
This script is for the ChlauApp application's entry point. 
"""

''' runapp.py
'''
import sys
import os
from dotenv import load_dotenv
from os import environ
# from ChlauApp import app, views, models
from ChlauApp import create_app

if __name__ == '__main__':
    app = create_app()
    
    #####################################
    #  Development settings
    # 
    ## Check Python at lease version 3.10
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
        print("Python 3.10 or higher is required.")
        sys.exit(1)    # fail. 
    else:
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} is running")

    ################################
    #  Production settings
    #
    app.run()
    
    

