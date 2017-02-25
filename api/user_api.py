from flask import *
from extensions import connect_to_database 
import hashlib
import uuid
import re

user_api = Blueprint('user_api', __name__, template_folder='templates')

@user_api.route('/api/user',methods=['GET','POST','PUT'])
def user_api_route():
    if request.method == 'GET':
        if 'username' in session:
            print("success get, with session")
            db = connect_to_database()
            cur = db.cursor()
            cur.execute("SELECT * FROM User WHERE username = '%s'" %(session['username']))
            userInfo = cur.fetchone()
            dict = {
                "username": userInfo['username'],
                "firstname": userInfo['firstname'],
                "lastname": userInfo['lastname'],
                "email": userInfo['email']
            }
            db.close()
            return jsonify(dict),200
        else:
            print("error get")
            error = {
                "errors":[
                    {
                        "message": "You do not have the necessary credentials for the resource"
                    }
                ]
            }
            return jsonify(error),401
    elif request.method == 'POST':
        print("enter post")
        needed_keys = ['username', 'firstname', 'lastname', 'password1', 'password2', 'email']
        form = request.get_json()
        print(form)
        enough = True
        for key in needed_keys:
            if (key not in form):
                enough = False
                break

        if (enough):
            print("enough post parameters")
            result = signup_check(form,check_username = True, check_pass = True)
            if (result[0] == True):
                print("success_post")
                # register for the new user and return the same form back
                password_hash = hashword(form["password1"])
                db = connect_to_database()
                cur = db.cursor()
                cur.execute("INSERT INTO User(username,firstname,lastname,password,email) VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" \
                    %(form["username"], form["firstname"], form["lastname"], password_hash, form["email"]))
                db.close()
                return jsonify(form),201

            else:
                error = result[1]
                return jsonify(error),422
        else:
            print("error_post")
            error = {
                "errors":[
                    {
                        "message": "You did not provide the necessary fields"
                    }
                ]
            }
            return jsonify(error),422
    elif request.method == 'PUT':
        if 'username' in session:
            print("has session in put")
            needed_keys = ['username', 'firstname', 'lastname', 'password1', 'password2', 'email']
            form = request.get_json()
            enough = True
            for key in needed_keys:
                if (key not in form):
                    enough = False
                    break
            if (enough):
                print("enough parameters in put")
                if (session['username'] != form['username']):
                    error = {"errors":[{"message": "You do not have the necessary permissions for the resource"}]}
                    return jsonify(error),403
                else:
                    if (form['password1'] == "" and form['password2'] == ""):
                        result = signup_check(form, check_username = False, check_pass = False)
                    else:
                        result = signup_check(form, check_username = False, check_pass = True)
                    if (result[0] == True):
                        db = connect_to_database()
                        cur = db.cursor()
                        if (form['password1'] == "" and form['password2'] == ""):
                            cur.execute("UPDATE User SET firstname = '%s', lastname = '%s', email = '%s' WHERE username = '%s'" \
                                %(form["firstname"], form["lastname"], form["email"], form["username"]))
                        else:
                            password_hash = hashword(form['password1'])
                            cur.execute("UPDATE User SET firstname = '%s', lastname = '%s', email = '%s', password = '%s' WHERE username = '%s'" \
                                %(form["firstname"], form["lastname"], form["email"], password_hash, form["username"]))
                        cur.close()
                        return jsonify(form),201

                    else:
                        error = result[1]
                        return jsonify(error),422
            else:
                print("not enough parameters in put")
                error = {
                    "errors":[
                        {
                            "message": "You did not provide the necessary fields"
                        }
                    ]
                }
                return jsonify(error),422

        else:
            print("no session in put")
            error = {
                "errors":[
                    {
                        "message": "You do not have the necessary credentials for the resource"
                    }
                ]
            }
            return jsonify(error),401

def signup_check(form, check_username, check_pass):
    username = form['username']
    firstname= form['firstname']
    lastname = form['lastname']
    password1 = form['password1']
    password2 = form['password2']
    email= form['email']
    valid = True
    db = connect_to_database()
    cur = db.cursor()
    # test existance for username
    cur.execute("SELECT * FROM User WHERE username = '%s'" %(form['username']))
    error = {
        "errors":[]
    }

    # test length of username
    if (check_username):
        if (cur.fetchone() != None):
            tmp = [{"message": "This username is taken"}]
            error['errors'] += tmp
            valid = False
        if (len(username) > 20):
            tmp = [{"message": "Username must be no longer than 20 characters"}]
            error['errors'] += tmp
            valid = False
        elif (len(username) < 3):
            tmp = [{"message": "Usernames must be at least 3 characters long"}]
            error['errors'] += tmp
            valid = False
        # test letters in username
        if re.search('\W',username):
            tmp = [{"message": "Usernames may only contain letters, digits, and underscores"}]
            error['errors'] += tmp
            valid = False

    # test firstname
    if (len(firstname) > 20):
        tmp = [{"message": "Firstname must be no longer than 20 characters"}]
        error['errors'] += tmp
        valid = False        
    # test lastname
    if (len(lastname) > 20):
        tmp = [{"message": "Lastname must be no longer than 20 characters"}]
        error['errors'] += tmp
        valid = False
    # test password
    if (check_pass):
        if (len(password1) < 8):
            tmp = [{"message": "Passwords must be at least 8 characters long"}]
            error['errors'] += tmp
            valid = False

        if re.search('\W',password1):
            tmp = [{"message": "Passwords may only contain letters, digits, and underscores"}]
            error['errors'] += tmp
            valid = False

        if re.match("^[a-zA-Z]*$",password1) or re.match("^[0-9]*$",password1):
            tmp = [{"message": "Passwords must contain at least one letter and one number"}]
            error['errors'] += tmp
            valid = False

        if (password1 != password2):
            tmp = [{"message": "Passwords do not match"}]
            error['errors'] += tmp
            valid = False

    # test email
    if (len(email) > 40):
        tmp = [{"message": "Email must be no longer than 40 characters"}]
        error['errors'] += tmp
        valid = False

    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        tmp = [{"message": "Email address must be valid"}]
        error['errors'] += tmp
        valid = False
    db.close()    
    return valid, error
    
def hashword(password1):
    algorithm = 'sha512'
    salt = uuid.uuid4().hex  
    m = hashlib.new(algorithm)
    m.update(str(salt + password1).encode('utf-8'))
    password_h=m.hexdigest()
    password_hashs="$".join([algorithm,salt,password_h])
    return password_hashs
