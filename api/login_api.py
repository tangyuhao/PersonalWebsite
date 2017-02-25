from flask import *
from extensions import connect_to_database 
import hashlib
import uuid

login_api = Blueprint('login_api', __name__, template_folder='templates')

@login_api.route('/api/login',methods=['POST'])
def login_api_route():
    if request.method == 'POST':
        needed_keys = ['username','password']
        #print(needed_keys)
        form = request.get_json()
        enough = True
        for key in needed_keys:
            if (key not in form):
                enough = False
                break
        if (enough):
                print("enough")
                db = connect_to_database()
                cur = db.cursor()
                cur.execute('SELECT username, password FROM User WHERE username = \'%s\'' %(form['username']))
                user_flag = cur.fetchone()
                print(user_flag)
                if user_flag:
                    pw_split = user_flag['password'].split("$")#choose the password in the database
                    pw_salt = pw_split[1]
                    pw_req = salt_hash_chk(pw_salt,form['password'])
                    print("test")
                                        #use the password and salt to generate a new password
                    if pw_req == user_flag['password']:
                        print("success")
                        session['username'] = form['username']
                        dict = {
                            "username": form['username']
                        }
                        return jsonify(dict)
                    else:
                        error = {
                            "errors":[
                                {
                                    "message":"Password is incorrect for the specified username"
                                }
                            ]
                        }
                        return jsonify(error),422
                else:
                    error = {
                        "errors":[
                            {
                                "message": "Username does not exist"
                            }
                    ]
                            }
                    return jsonify(error),404
        else:
            error = {
                "errors":[
                    {
                        "message": "You did not provide the necessary fields"
                    }
                ]
            }
            return jsonify(error),422

def salt_hash_chk(salt,password):
    algorithm = 'sha512'     # name of the algorithm to use for encryption
    m = hashlib.new(algorithm)
    m.update(str(salt + password).encode('utf-8'))
    password_hash = m.hexdigest()
    return ("$".join([algorithm,salt,password_hash]))

           

