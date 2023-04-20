#!/usr/bin/python3
"""
This python scrip starts a wev application rhat run on the host
0.0.0.0 and port 5000
Args:
    route "/": display "Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet_hbnb():
    """prints greeting message to our hbnb
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
