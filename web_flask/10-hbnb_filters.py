#!/usr/bin/python3
"""
qeb frame work: creating a web apllication to list state and citis
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    removes current session after use
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def state_filters():
    """displays a scrollable page containing a list of cities and states
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    render_template("10-hbnb_filters.html", st=states, amen=amenities)


if __name__ == "__main__":
    app.run(host="0..0.0.0", port=5000)
