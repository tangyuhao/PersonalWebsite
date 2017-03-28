# -*- coding: utf-8 -*-
from flask import *
import os
from extensions import connect_to_database 
article_api = Blueprint('article_api', __name__, template_folder='templates')

@article_api.route('/api/article',methods=['POST'])
def article_api_func():
    if request.method == 'POST':
        form = request.get_json()
        if (form["cmd"] == "delete"):
            print(form["articleid"])

        db = connect_to_database()
        
        cmd = "DELETE FROM Article WHERE articleid=%s"
        if ('username' not in session or session['username']!="yuhaotang"):
            return jsonify({"error:": "no permission to delete an article"}), 403

        cur = db.cursor()
        cur.execute("SELECT * from Article Where articleid=\"%s\"" %(form["articleid"]))
        result = cur.fetchone()
        print(os.path.join("./assets/blog/images/",result["cover_img"]))

        os.remove(os.path.join("./assets/blog/images/",result["cover_img"]))
        os.remove(os.path.join("./assets/blog/articles/",result["articleid"]+".html"))


        try:
            cur.execute(cmd,(form['articleid']))
        except:
            return jsonify({"error": "internal error"}),500

        cur = db.cursor()
        return jsonify(form),200

