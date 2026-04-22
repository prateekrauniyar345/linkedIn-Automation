from flask import Flask, jsonify, request
import os
import datetime

app = Flask(__name__)


# defualt route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Google Sheets API!",
        "timestamp": datetime.datetime.now().isoformat(), 
        "status" : "running" 
    })


if '__main__' == __name__:
    app.run(host="0.0.0.0")