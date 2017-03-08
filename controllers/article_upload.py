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


article_upload = Blueprint('article_upload', __name__, template_folder='templates')

@article_upload.route('/article_upload',methods=['GET','POST'])
def upload_article_route():
    db = connect_to_database()
    cur = db.cursor()
    cur.execute("SELECT title,blogid FROM Blog")
    blogs = cur.fetchall()
    article_uploaded = False
    if request.method == 'POST':
        article_uploaded = True
        # form:
        # {title:xxx, abstract: xxx, content: xxx, blog_name: xxx, img: (file)}
        if ('username' not in session or session['username']!="yuhaotang"):
            return("error: not logged in or not permitted")
        form = request.form
        files = request.files
        status, mesg, ret_code = check_upload_valid(form,files,db)
        if (status == False):
            options = {
                "blogs": blogs,
                "form": form,
                "message": mesg
            }
            return render_template("article_upload.html",**options)
    if ('username' not in session or session['username'] != "yuhaotang"):
        abort(404)
    else:
        if (article_uploaded):
            options = {
                "message": mesg,
                "blogs": blogs
            }
        else:
            options = {
                "blogs": blogs
            }
        return render_template("article_upload.html", **options)

def check_upload_valid(form,files,db):
    needed_key = ['title', 'abstract', 'content', 'blogid']
    for key in needed_key:
        if key not in form:
            return False,"ERROR: no enough form elements", 422
    if "img_file" not in files:
        return False, "ERROR: no image file", 422
    else:
        for key in needed_key:
            if form[key] == '':
                return False, "ERROR: empty input is not allowed", 422

        orig_file = files['img_file']
        if orig_file and allowed_file(orig_file.filename):
            filename = secure_filename(orig_file.filename) # prevent injection, do not accept chinese charactors
        else:
            return False, "ERROR: file not allowed or not uploaded", 422
        img_name = title_hash(filename)
        img_name_split = os.path.splitext(filename)
        ext = img_name_split[1]
        if (not ext):
            return False, "ERROR: image filename wrong", 500
        img_name_ext = img_name+ext
        orig_file.save(os.path.join(UPLOAD_FOLDER,img_name_ext))
        file_name = title_hash(form["title"])
        try:
            f = codecs.open(os.path.join(CONTENT_FOLDER,file_name + ".html"),"w+","utf-8")
        except:
            f.close()
            return False, "ERROR:create file failed", 500
        f.write(form['content'])
        f.close()
        cur = db.cursor()
        cmd = "INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES (%s,%s,%s,%s,%s)"
        cur.execute(cmd, (file_name,form["blogid"],form["title"],form["abstract"],img_name_ext))
        return True, "SUCCESS", 200





def title_hash(title):
    algorithm = 'sha1'     # name of the algorithm to use for encryption
    m = hashlib.new(algorithm)
    salt = uuid.uuid4().hex
    m.update(str(salt + title).encode('utf-8'))
    outputid = m.hexdigest()
    return (outputid)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@article_upload.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404
