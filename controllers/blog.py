from flask import *

blog = Blueprint('blog', __name__, template_folder='templates')
@blog.route('/blog') 
def show_bloghome():
        options = {

        }
        return render_template("bloghome.html",**options)

@blog.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404