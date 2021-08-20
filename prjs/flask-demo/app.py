import socket
from flask_cors import *
from flask import Flask, jsonify
import redis

app = Flask(__name__, static_folder='app', static_url_path="/app")
CORS(app, supports_credentials=True)

r = redis.Redis(host='redis-service', port=6379)


@app.route("/count")
def count():
    count_num = int(r.get('count_num'))
    if not count_num:
        count_num = 0
    count_num += 1
    r.set('count_num', count_num)
    return jsonify({
        "count_num": int(count_num),
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
        port=6000,
        debug=True
    )
