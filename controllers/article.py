# -*- coding: utf-8 -*-
from flask import *
from extensions import connect_to_database 
import codecs

article = Blueprint('article', __name__, template_folder='templates')

@article.route('/article') 
def show_test():
    articleid = request.args.get('articleid')
    if (not articleid):
        abort(404)
    else:
        db = connect_to_database()
        cur = db.cursor()
        cmd = "SELECT *,DATE_FORMAT(created,'%%b %%d, %%Y') AS date FROM Article WHERE articleid=%s"
        cur.execute(cmd, (articleid))
        article = cur.fetchone()
        if (not article):
            abort(404)
        else:
            file_name = articleid + ".html"
            try:
                article_file = codecs.open("./assets/blog/articles/" + file_name,"r","utf-8") 
            except:
                abort(404)
            cur = db.cursor()
            cur.execute("SELECT * FROM Blog WHERE blogid=%d" %(article["blogid"]))
            blog_name = cur.fetchone()["title"]
            article["blogTitle"] = blog_name

            cur = db.cursor()

            content = article_file.read()
            options = {
                "articleid": articleid,
                "codeHighlight": True,
                "article_info": article,
                "content": content,
                "isArticle": True
            }
            return render_template("article.html",**options)
