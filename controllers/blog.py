from flask import *
from extensions import connect_to_database 

blog = Blueprint('blog', __name__, template_folder='templates')
@blog.route('/blog') 
def show_bloghome():
    options = {

    }
    return render_template("bloghome.html",**options)

@blog.route('/article') 
def show_test():
    articleid = request.args.get('articleid')
    if (not articleid):
        abort(404)
    else:
        db = connect_to_database()
        cur = db.cursor()
        cur.execute("SELECT * FROM Article WHERE articleid='%s'" %(articleid))
        article = cur.fetchone()
        if (not article):
            abort(404)
        else:
            file_name = articleid + ".html"
            try:
                article_file = open("./assets/blog/articles/" + file_name,"r") 
            except:
                abort(404)
            content = article_file.read()
            options = {
                "codeHighlight": True,
                "article_info": article,
                "content": content
            }
            return render_template("article.html",**options)



@blog.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404