from flask import *
from extensions import connect_to_database 
from werkzeug.utils import secure_filename
import hashlib
import uuid
import os

UPLOAD_FOLDER = 'assets/blog/images'
CONTENT_FOLDER = 'assets/blog/articles'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


article_upload = Blueprint('article_upload', __name__, template_folder='templates')

@article_upload.route('/article_upload',methods=['GET','POST'])
def upload_article_route():
    if request.method == 'POST':
        # form:
        # {title:xxx, abstract: xxx, content: xxx, blog_name: xxx, img: (file)}
        if ('username' not in session or session['username']!="yuhaotang"):
            return("error: not logged in or not permitted")
        form = request.form
        db = connect_to_database()
        if 'img_file' not in request.files:
            return ("error:no image file"),422
        orig_name = request.files['img_file']
        if orig_name.filename == '':
            return redirect("error:no image file name"),422
        if orig_name and allowed_file(orig_name.filename):
            # print(orig_name.filename)
            filename = secure_filename(orig_name.filename)
            print(filename)
            img_name = title_hash(filename)
            img_name_split = os.path.splitext(filename)
            ext = img_name_split[1]
            if (not ext):
                return ("error: filename wrong"),500
            img_name_ext = img_name+ext
            orig_name.save(os.path.join(UPLOAD_FOLDER,img_name_ext))
            try:
                file_name = title_hash(form["title"])
                f = open(os.path.join(CONTENT_FOLDER,file_name + ".html"),"w+")
                f.write(form["content"])
                f.close()
            except:
                return ("error:create file failed"),500

            cur = db.cursor()
            cmd = "SELECT blogid FROM Blog WHERE title = %s"
            cur.execute(cmd,(form["blog_name"]))
            print("OK")
            bloginfo = cur.fetchone()
            if (not bloginfo):
                return ("error: cannot find this blog class"),404
            else:
                cur = db.cursor()
                cmd = "INSERT INTO Article(articleid, blogid, title, abstract, cover_img) VALUES (%s,%s,%s,%s,%s)"
                cur.execute(cmd, (file_name,bloginfo["blogid"],form["title"],form["abstract"],img_name))
    if ('username' not in session or session['username']!="yuhaotang"):
        print("wrong")
        abort(404)
    else:
        print("ok")
        return render_template("article_upload.html")




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