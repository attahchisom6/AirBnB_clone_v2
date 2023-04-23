#!/usr/bin/python3
"""
web framework creating a web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    delete curent session once its done
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def show_states():
    """displays list of all available states in the current session
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_by_id_contains_city(id):
    """This will list all states whoses id matches the given id
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
