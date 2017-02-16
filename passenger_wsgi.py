import sys, os
INTERP = os.path.join(os.environ['HOME'],'.pyenv', 'versions', 'webserver', 'bin', 'python')
print(INTERP)
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
    sys.path.append(os.getcwd())

#from flask import Flask
#application = Flask(name)



#@application.route('/')
#def index():
#        return 'Hello Passenger'
from app import app as application
# Comment out the next two lines to disable debugging when your app is ready
#from werkzeug.debug import DebuggedApplication
#application = DebuggedApplication(application, evalex=True)

