# -*- coding: utf-8 -*-
from flask import *

logout = Blueprint('logout', __name__, template_folder='templates')

@logout.route('/logout')
def logout_route():
    if "username" in session:
        print("logout...")
        session.pop('username', None)
        return redirect(url_for('main.show_homepage'))
    else:
        abort(401)

