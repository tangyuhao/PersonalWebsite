from flask import *
from extensions import connect_to_database 

logout_api = Blueprint('logout_api', __name__, template_folder='templates')
@logout_api.route('/api/logout',methods=['POST'])
def logout_api_route():
    if request.method == 'POST':
        if 'username' in session:
            session.pop('username', None)
            return jsonify(),204
        else:
            error = {
                "errors":[
                    {
                        "message": "You do not have the necessary credentials for the resource"
                    }
                ]
            }
            return jsonify(error),401