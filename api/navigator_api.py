from flask import *
from extensions import connect_to_database 

navigator_api = Blueprint('navigator_api', __name__, template_folder='templates')

@navigator_api.route('/api/nav/topnavbar',methods=['GET'])
def topnavbar_api_route():
    if request.method == 'GET':
        db = connect_to_database()
        cur = db.cursor()
        ret_dict = {}
        cur.execute("SELECT * FROM BlogGroup")
        BlogGroups = cur.fetchall()
        blog_part = {}
        for group in BlogGroups:
            cur = db.cursor()
            cur.execute("SELECT title,blogid FROM Blog WHERE groupid=%d ORDER BY title ASC" %(group["groupid"]))
            blog_part[group["title"]] = cur.fetchall()
        cur = db.cursor()
        cur.execute("SELECT title,albumid FROM Album")
        photography_part = cur.fetchall()
        ret_dict["Blog"] = blog_part;
        ret_dict["Photography"] = photography_part;
        return jsonify(ret_dict),200
@navigator_api.route('/api/nav/articles/<blog>&<infotype>',methods=['GET'])
def all_articles_api_route(blog,infotype):
    if request.method == 'GET':
        db = connect_to_database()
        if (blog == "all"):
            cur = db.cursor()
            if (infotype == "with_abstract"):
                cur.execute("SELECT * FROM Article ORDER BY lastupdated DESC")
            else:
                # should be no_abstract, but others are all fine
                cur.execute("SELECT articleid,author,blogid,created,lastupdated,title FROM Article ORDER BY lastupdated DESC")
            ret_list = cur.fetchall()
            return jsonify({"articles":ret_list}),200
        else:
            if (blog.isdigit()):
                blog = int(blog)
                cur = db.cursor()
                cur.execute("SELECT * FROM Blog WHERE blogid=%d" %(blog))
                if (not cur.fetchall()):
                    return jsonify({}),404
                cur = db.cursor()
                if (infotype == "with_abstract"):
                    cur.execute("SELECT * FROM Article WHERE blogid=%d ORDER BY lastupdated DESC" %(blog))
                else:
                    # should be no_abstract, but others are all fine
                    cur.execute("SELECT articleid,author,blogid,created,lastupdated,title FROM Article WHERE blogid=%d ORDER BY lastupdated DESC" %(blog))
                ret_list = cur.fetchall()
                return jsonify({"articles":ret_list}),200
            else:
                return jsonify({}),404



  