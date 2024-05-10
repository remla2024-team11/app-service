from flask import Flask, request, jsonify
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Dummy database to store data
data = []

@app.route('/api/post', methods=['POST'])
def add_data():
    try:
        new_data = request.json
        
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_data)
        print(response.json())
        if response.status_code == 200 or response.status_code == 201:
            data.append(new_data)
            return jsonify({'message': 'Data added successfully', 'data': response.json()}), 201
        else:
            return jsonify({'message': 'Error adding data to the other API'}), response.status_code
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)