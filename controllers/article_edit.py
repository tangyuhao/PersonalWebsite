# -*- coding: utf-8 -*-
from flask import *
from extensions import connect_to_database 
from werkzeug.utils import secure_filename
import hashlib
import uuid
import os
import codecs

UPLOAD_FOLDER = 'assets/blog/images'
CONTENT_FOLDER = 'assets/blog/articles'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


article_edit = Blueprint('article_edit', __name__, template_folder='templates')

@article_edit.route('/article/edit',methods=['GET','POST'])
def edit_article_route():
    articleid = request.args.get('articleid')
    if ('username' not in session or session['username'] != "yuhaotang" or not articleid):
        abort(404)
    db = connect_to_database()
    cur = db.cursor()
    cur.execute("SELECT * FROM Article WHERE articleid=\"%s\"" %(articleid))
    article_info = cur.fetchone()
    if (not article_info):
        abort (404)

    cur = db.cursor()
    cur.execute("SELECT title,blogid FROM Blog")
    blogs = cur.fetchall()

    if request.method == 'POST':
        article_uploaded = True
        # form:
        # {title:xxx, abstract: xxx, content: xxx, blog_name: xxx, img: (file)}
        form = request.form
        files = request.files
        status, mesg, ret_code = check_upload_valid(form,files,article_info,db)
        if (status == False):
            form = form.to_dict()
            form['blogid'] = int(form['blogid'])
            options = {
                "blogs": blogs,
                "content": form['content'],
                "message": mesg,
                "article_info": form
            }

            return render_template("article_edit.html",**options)
        else:
            options = {"blogid":form["blogid"]}
            return redirect(url_for('blog.show_blog', **options))

    f = codecs.open("./assets/blog/articles/" + article_info["articleid"] + ".html","r","utf-8")
    content = f.read()
    f.close()
    
    options = {
        "blogs": blogs,
        "content": content,
        "article_info": article_info
    }
    return render_template("article_edit.html", **options)


    # make sure that user has permission to edit the article
    

def check_upload_valid(form,files,article_info,db):
    needed_key = ['title', 'abstract', 'content', 'blogid']
    for key in needed_key:
        if key not in form:
            return False,"ERROR: no enough form elements", 422
    for key in needed_key:
        if form[key] == '':
            return False, "ERROR: empty input is not allowed", 422
    if ('img_file' in files and files['img_file'] and files['img_file'].filename != ''):        
        orig_file = files['img_file']
        if allowed_file(orig_file.filename):
            filename = secure_filename(orig_file.filename) # prevent injection, do not accept chinese charactors
        else:
            return False, "ERROR: file not allowed", 422
        orig_file.save(os.path.join(UPLOAD_FOLDER,article_info["cover_img"]))

    try:
        f = codecs.open(os.path.join(CONTENT_FOLDER,article_info["articleid"] + ".html"),"w+","utf-8")
    except:
        f.close()
        return False, "ERROR:create file failed", 500
    f.write(form['content'])
    f.close()
    cur = db.cursor()
    cmd = "UPDATE Article SET blogid=%s, title=%s, abstract=%s WHERE articleid=%s"
    cur.execute(cmd, (form["blogid"],form["title"],form["abstract"],article_info["articleid"]))
    # when change the article to other catagory.
    if (int(form['blogid']) != article_info['blogid']):
        # print("change blog group")
        # print(form['blogid'])
        # print(article_info)
        cur = db.cursor()
        cur.execute("UPDATE Blog SET article_num = article_num + 1 WHERE blogid=%d" %(int(form["blogid"])))
        cur = db.cursor()
        cur.execute("UPDATE Blog SET article_num = article_num - 1 WHERE blogid=%d" %(article_info["blogid"]))
    return True, "SUCCESS", 200






def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@article_edit.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404
