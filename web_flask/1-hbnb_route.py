#!/usr/bin/python3
"""
atarts a web application that listens on poet 5000 and host 0.0.0.0

routes:
    "/": displays 'Hello HBNB!'
    "/hbnb": displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet_hbnb():
    """greet objs urls spxified in the route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns the string 'hbnb' on this path
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
