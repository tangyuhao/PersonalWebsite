from flask import Flask, render_template
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates', static_folder='assets')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register the controllers
app.secret_key = '7UOCc\x07\xe2vz\x8b\xdf\x08y[\xce\xd2SI\x0c\xda%b\xd9N'
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.blog)


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(port=3000,host='0.0.0.0',debug=True)

