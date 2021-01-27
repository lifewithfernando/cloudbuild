# app.py

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world. 21-01-27, 22:00"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
