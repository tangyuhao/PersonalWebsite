from flask import *
from extensions import connect_to_database 
import math

NUM_EACHPAGE = 5
PAGES_EACHBAR = 5

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/blog') 
def show_blog():
    blogid = request.args.get('blogid')
    if (not blogid):
        blogid = 0
    elif (blogid.isdigit()):
        blogid = int(blogid)
    else:
        abort(404)
    page = request.args.get('page')
    if (not page):
        page = 1
    elif (page.isdigit()):
        page = int(page)
    else:
        abort(404)
    # now get page and blogid


    db = connect_to_database()
    if (blogid == 0):
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM Article")
        count = cur.fetchone()["COUNT(*)"]
        if (NUM_EACHPAGE * page - NUM_EACHPAGE >= count):
            abort(404)
        cur = db.cursor()
        cur.execute("SELECT *,DATE_FORMAT(created,'%%b %%d, %%Y') AS date FROM Article ORDER by lastupdated DESC LIMIT %d,%d;" \
            %(NUM_EACHPAGE*page - NUM_EACHPAGE,NUM_EACHPAGE))
        articles = cur.fetchall()

    else: # blogid not 0
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM Article WHERE blogid=%d" %(blogid))
        count = cur.fetchone()["COUNT(*)"]
        if (NUM_EACHPAGE * page - NUM_EACHPAGE >= count):
            abort(404)
        cur = db.cursor()
        cur.execute("SELECT *,DATE_FORMAT(created,'%%b %%d, %%Y') AS date FROM Article WHERE blogid=%d ORDER by lastupdated DESC LIMIT %d,%d;" \
            %(blogid,NUM_EACHPAGE*page - NUM_EACHPAGE,NUM_EACHPAGE))
        articles = cur.fetchall()

    cur = db.cursor()
    cur.execute("SELECT blogid,title FROM Blog")
    blogs = cur.fetchall()
    blogs_table = {}
    for blog in blogs:
        blogs_table[blog["blogid"]] = blog["title"]
    page_navbar = math.ceil(page/PAGES_EACHBAR) 
    max_page = math.ceil(count/NUM_EACHPAGE)
    print(max_page)
    max_page_navbar = math.ceil(max_page/PAGES_EACHBAR)
    start = page_navbar * PAGES_EACHBAR - PAGES_EACHBAR + 1
    end = min(max_page, start + PAGES_EACHBAR) + 1
    page_range = list(range(start,end))
    options = {
        "articles": articles,
        "page": page,
        "page_navbar": page_navbar,
        "max_page_navbar": max_page_navbar,
        "NUM_EACHPAGE": NUM_EACHPAGE,
        "PAGES_EACHBAR": PAGES_EACHBAR,
        "blogs_table": blogs_table,
        "blogid": blogid,
        "page_range": page_range
    }
    return render_template("blog.html",**options)


@blog.errorhandler(404)
def page_not_found(e):
    options = {
        'isError':True
    }
    return render_template('404error.html',**options), 404