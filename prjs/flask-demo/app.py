from flask import Flask, jsonify

app = Flask(__name__, static_folder='app', static_url_path="/app")


@app.route("/")
def heartbeat():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=6000,
        debug=True
    )
