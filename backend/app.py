from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/message')
def message():
    return jsonify({
        "message": "🚀 Hello from Backend! Database connected successfully! - Kishore DevOps Project"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "Backend is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
