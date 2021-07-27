import socket

from flask import Flask, jsonify

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route("/")
def heartbeat():
    return jsonify({
        "status": "healthy",
        "version": "v1.0.2",
    })


@app.route("/ip")
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=6000,
        debug=True
    )
