from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from lib_version_team11 import VersionUtil

load_dotenv()

import os
MODEL_API = os.getenv("MODEL_API")
FRONTEND= os.getenv("FRONTEND")

app = Flask(__name__)
# CORS(app, resources={"/api/*": {"origins": FRONTEND}})
CORS(app)

# Dummy database to store data
data = []

@app.route('/api/post', methods=['POST'])
def add_data():
    try:
        new_data = request.json
        headers = {
            'Content-type': 'application/json; charset=UTF-8'
        }
        response = requests.post(MODEL_API, json=new_data, headers=headers)
        print(response.json())
        if response.status_code == 200 or response.status_code == 201:
            data.append(new_data)
            return jsonify({'message': 'Data added successfully', 'data': response.json()}), 201
        else:
            return jsonify({'message': 'Error adding data to the other API'}), response.status_code
    except Exception as e:
        return jsonify({'message': f'Error:{MODEL_API} {str(e)}'}), 400

@app.route('/api/version', methods=['GET'])
def getVersion():
    print(request.url)
    version = VersionUtil.get_version()
    return jsonify({'version': version})

if __name__ == '__main__':
    app.run(debug=True)