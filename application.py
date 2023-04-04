from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def multiple_files():
    keys = ['name', 'age', 'email', 'phone']
    values = ['John Doe', 25, 'john.doe@example.com', '+1-555-555-5555']
    data = {}
    for i in range(len(keys)):
        data[keys[i]] = values[i]
    return jsonify(data)
