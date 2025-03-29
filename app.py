from flask import Flask, request, jsonify, send_from_directory
import os
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# File to store waitlist emails
WAITLIST_FILE = os.environ.get('WAITLIST_FILE', 'waitlist_data.json')

# Initialize waitlist file if it doesn't exist
if not os.path.exists(WAITLIST_FILE):
    with open(WAITLIST_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/waitlist', methods=['POST'])
def add_to_waitlist():
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({'error': 'Email is required'}), 400
    
    email = data['email']
    
    # Simple validation
    if not '@' in email or not '.' in email:
        return jsonify({'error': 'Invalid email format'}), 400
    
    # Load existing waitlist
    with open(WAITLIST_FILE, 'r') as f:
        waitlist = json.load(f)
    
    # Check if email already exists
    for entry in waitlist:
        if entry['email'] == email:
            return jsonify({'error': 'Email already registered'}), 409
    
    # Add new email
    waitlist.append({
        'email': email,
        'date': datetime.now().strftime('%Y-%m-%d')
    })
    
    # Save updated waitlist
    with open(WAITLIST_FILE, 'w') as f:
        json.dump(waitlist, f)
    
    return jsonify({
        'success': True,
        'message': 'Email added to waitlist',
        'count': len(waitlist)
    })

@app.route('/api/waitlist', methods=['GET'])
def get_waitlist():
    # In a production app, this would be protected with authentication
    with open(WAITLIST_FILE, 'r') as f:
        waitlist = json.load(f)
    
    return jsonify({
        'count': len(waitlist),
        'entries': waitlist
    })

if __name__ == '__main__':
    # Use environment variables for port with fallback to 8000
    port = int(os.environ.get('PORT', 8000))
    # Only use debug mode in development
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port) 