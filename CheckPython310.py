## Check Python at lease version 3.10

import sys

if not sys.version_info.major == 3 and sys.version_info.minor >= 10:
	print("Python 3.10 or higher is required."
	print("You are using Python {}.{}. ".format(sys.version_info_major, sys.version_info.minor))
	sys.exit(1)    # fail. 

