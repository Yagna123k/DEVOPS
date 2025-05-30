from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

File = 'data.json'

@app.route('/')
def home():
    return "Welcome to the Flask Task 1.."

@app.route('/api', methods=['GET'])
def get_data():
    if not os.path.exists(File):
        return jsonify({"error": "Data file not found"}), 404
    
    try:
        with open(File, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)