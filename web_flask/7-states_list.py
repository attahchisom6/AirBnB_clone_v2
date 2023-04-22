#!/usr/bin/python3
"""
script to build a web application
"""
from flask import Flask
from models import storage
from models.state import State

Flask(__name__)


@app.route("/state_list", strict_slashes=False)
def show_states(self):
    """display a list of states we currently have at the moment
    """
    states = storage.all(States).values()
    return render_template("7-states_list.html", st=states)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
