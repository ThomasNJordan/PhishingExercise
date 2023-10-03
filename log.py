from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # Allow requests from your HTML page's origin

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    
    print(data)
    # Process the data (e.g., write it to a file)
    with open('user_input.txt', 'a') as file:
        file.write(data['password'] + '\n')
    
    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(port=8000)
