#!/usr/bin/python3
"""
Script to imitiate a web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet_hbnb():
    """
    function to return a greeting text
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return the string "HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_without_underscore(text):
    """prinnt the first argument inserted in the command line
    """
    txt = text.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python_text_without_underscore(text="is cool"):
    """print text without underacore, 'cool' is its default text
    """
    txt = text.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:n>", strict_slashes=False)
def print_integer(n):
    """
    orint out required string containing n if only n is an integer
    """
    num_txt = "{:d} is a number".format(n)
    return num_txt


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
