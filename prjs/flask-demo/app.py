import socket
from flask_cors import *
from flask import Flask, jsonify
import redis
import os

app = Flask(__name__, static_folder='app', static_url_path="/app")
CORS(app, supports_credentials=True)


if os.environ.get('REDIS_SERVER_HOST'):
    r_host = os.environ.get('REDIS_SERVER_HOST')
    r_desc = 'ENVIRON'
else:
    r_host = os.environ.get('172.17.0.3')
    r_desc = 'LOCAL'
# r = redis.Redis(host='172.17.0.3', port=6379)
# r.set('count_num', 1)
r = redis.Redis(host=r_host, port=6379)


@app.route("/count")
def count():
    if r.get('count_num'):
        count_num = int(r.get('count_num'))
    else:
        count_num = 0
    if not count_num:
        count_num = 0
    count_num += 1
    r.set('count_num', count_num)
    return jsonify({
        "count_num": int(count_num),
        'r_desc': r_desc,
        'r_host': r_host
    })


@app.route("/")
def heartbeat():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return jsonify({
        "status": "healthy",
        "version": "v1.0.2",
        "pod": ip
    })


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
