#!/usr/bin/python3
"""
script to build a web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_db(exc):
    """delete current session when its done
    """
    storage.close()

@app.route("/state_list", strict_slashes=False)
def show_states():
    """display a list of states we currently have at the moment
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
