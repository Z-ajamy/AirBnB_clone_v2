#!/usr/bin/python3
"""
Starts a Flask web application.
- /states: Displays a list of all State objects.
- /states/<id>: Displays a State object and its cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Fetches all State objects from storage, sorts them by name (A-Z),
    and passes the list to the template.
    """
    all_states = storage.all(State).values()
    
    sorted_states = sorted(all_states, key=lambda state: state.name)
    
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_detail(id):
    """
    Fetches a specific State object by its ID.
    If found, passes the State object to the template.
    If not found, passes None.
    """
    key = f"State.{id}"
    state = storage.all(State).get(key)
    
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
