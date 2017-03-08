# -*- coding: utf-8 -*-
from flask import *
from extensions import connect_to_database 
import hashlib
import uuid
analysis_api = Blueprint('analysis_api', __name__, template_folder='templates')

@analysis_api.route('/api/analysis/articles/<articleid>',methods=['GET'])
def analysis_article_api_route(articleid):
    if request.method == 'GET':
        if (not articleid):
            return jsonify({}),422
        else:
            db = connect_to_database()
            cur = db.cursor()
            cmd = "SELECT reading_num FROM Article WHERE articleid=%s"
            cur.execute(cmd,(articleid))
            info = cur.fetchone()
            if (not info):
                return jsonify({}),404
            else:
                num = info["reading_num"] + 1
                cur = db.cursor()
                cmd = "UPDATE Article SET reading_num = %s WHERE articleid=%s"
                cur.execute(cmd, (num,articleid))
                ret_dict = {
                    "reading_num": num,
                    "article_id": articleid
                }
                return jsonify(ret_dict),200

  
