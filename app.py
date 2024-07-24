from flask import Flask, request, jsonify, session
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from user import verify_user, create_user
from park import get_parks, create_park

def login_required(f):
  def verification_reply(*args, **kwargs):
    if session.get('logged_in') is None:
      return jsonify({'error': 'You must be logged in to create parks'}), 400
    return f(*args, **kwargs)
  return verification_reply

@app.route("/", methods=["GET"])
def home():
    parks = get_parks()
    return jsonify(
        {
            'Available parks': parks,
            'Please sign in to continue': ''
        }
    ), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' and 'password' not in data:
        return jsonify({'error': 'Missing required data'}), 400

    username = data['username']
    password = data['password']

    if verify_user(username, password):
        session['logged_in'] = True
        session['username'] = username
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401
    
@app.route('/logout', methods=['GET'])
def logout():
        if session.pop('logged_in', None):
            return jsonify({'message': 'Logout successful'}), 200
        else:
            return jsonify({'error': 'You aren\'t logged in'}), 401

@app.route('/create_user', methods=['POST'])
def user_creation():
    data = request.get_json()

    if not data or 'username' and 'password' not in data:
        return jsonify({'error': 'Missing required data'}), 400

    username = data['username']
    password = data['password']

    if create_user(username, password):
        return jsonify({'message': 'Account creation succesful'}), 200
    else:
        return jsonify({'error': 'Account creation failed'}), 401
    
@app.route('/create_park', methods=['POST'])
@login_required
def park_creation():
    data = request.get_json()

    if not data or 'park_name' not in data:
        return jsonify({'error': 'Missing required data'}), 400

    park_name = data['park_name']

    if create_park(park_name):
        return jsonify({'message': 'Park creation succesful'}), 200
    else:
        return jsonify({'error': 'Park creation failed'}), 401

# This has to be kept at the bottom of the requests so that the requests are recgonized by the server
if __name__ == "__main__":
    app.run(host=app.config['API_IP'], port=app.config['API_PORT'], debug=True)
