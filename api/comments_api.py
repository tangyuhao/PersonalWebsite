# -*- coding: utf-8 -*-
from flask import *
from extensions import connect_to_database 
comments_api = Blueprint('comments_api', __name__, template_folder='templates')

@comments_api.route('/api/comments',methods=['POST'])
def analysis_article_api_route():
    if request.method == 'POST':
        form = request.get_json()
        if (not check_valid(form)):
            return jsonify({"error": "not enough inputs"}),422

        db = connect_to_database()
        cur = db.cursor()
        cmd = "INSERT INTO Comments(articleid,name,content) VALUES(%s,%s,%s)"
        try:
            cur.execute(cmd,(form['articleid'],form['name'],form['content']) )
        except:
            return jsonify({"error": "internal error"}),500
        return jsonify(form),200

def check_valid(form):
    needed_item = ['content','articleid','name']
    if not form:
        return False

    for item in needed_item:
        if item not in form:
            return False
    return True
