from flask import *

main = Blueprint('main', __name__, template_folder='templates')
@main.route('/') 
@main.route('/<args>')
def show_homepage(args=None):
    if (not args):
        options = {
            'isHomePage':True
        }
        return render_template("home.html",**options)
    elif (".html" in args):
        abort(403)
    else:
        abort(404)
@main.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404
@main.errorhandler(403)
def page_under_development(e):
    options = {
        'isError':True
    }
    return render_template('403error.html',**options), 403
