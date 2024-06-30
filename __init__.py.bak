# install flask and others from requirements
# > Python -m pip install -r .\ChlauApp\requirements.txt

import sys
import flask

if not sys.version_info.major == 3 and sys.version_info.minor >= 10:
	print("Python 3.10 or higher is required.")
	print("You are using Python {}.{}. ".format(sys.version_info_major, sys.version_info.minor))
	sys.exit(1)    # fail. 

app = flask.Flask(__name__)
