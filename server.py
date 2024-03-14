from flask import Flask, request, send_file
from database import *
from backend_operations import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "i_am_ironman"  

init_db(app)

@app.route('/')
def home():
    return 'Image Background Removal API.'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return signup_function(email, password)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return login_function(email, password)

@app.route('/remove_background', methods=['POST'])
def remove_background():

    if 'image' not in request.files:
        return 'No file part', 400
    apiKey = request.form.get('apiKey')
    
    file = request.files['image']
    
    output = remove_background_function(apiKey,file)

    if output[1] == 200:
        return send_file(output[0], mimetype='image/png')
    
    return output
    


if __name__ == '__main__':
    app.run(debug=True)
