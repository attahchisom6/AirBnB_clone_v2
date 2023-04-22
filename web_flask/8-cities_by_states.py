#!/usr/bin/python3
"""
web frame: create web application to list cities in the state
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardowm(self):
    """removes the current sql session when it is done
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def show_states():
    """
    list all cities within a state in the current session
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", st=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
