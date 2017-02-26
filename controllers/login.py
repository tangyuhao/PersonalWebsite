from flask import *
from extensions import connect_to_database 

login = Blueprint('login', __name__, template_folder='templates')
@login.route('/login')
def login_route():
    if ("username" in session):
        return redirect(url_for('main.show_homepage'))
    else:
        return render_template('login.html')

@login.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404
@login.errorhandler(403)
def page_under_development(e):
    options = {
        'isError':True
    }
    return render_template('403error.html',**options), 403
