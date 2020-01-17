from flask import Flask, request, Response, stream_with_context, jsonify
from redis import Redis
import os, time, json
app = Flask(__name__)
db = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    db.incr('count')
    return 'Count is %s.' % db.get('count')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)