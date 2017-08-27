#!flask/bin/python

"""
In response to a GET request to /, your server should inspect the Accept header sent by the client and:

If the request sends does not send an Accept header, your server responds with: 
<p>Hello, World</p>

If the incoming request sets an Accept header with value application/json, your server responds with:
{"message": "Good morning"}


"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    
    if request.method == 'GET':
        if request.headers['accept'] == 'application/json':
            return '{"message": "Good morning"}'
        else:
            return '<p>Hello, World</p>'


if __name__ == '__main__':
    app.run(debug=True)
