"""
This script is for the ChlauApp application's entry point. 
"""

''' runapp.py
'''
import sys
from ChlauApp import create_app

if __name__ == '__main__':

    #####################################
    ## Check Python at lease version 3.10
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} is running")
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):
        print("*** Python 3.10 or higher is required ***")
        sys.exit(1)    # fail. 
        
    app = create_app()
    app.run()
    
    

