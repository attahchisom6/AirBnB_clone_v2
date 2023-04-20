#!/usr/bin/python3
"""
Script to imitiate a web application
"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    displays html content if only n is an integer
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    displays a html page entailing if a number is odd or even
    """
    return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
