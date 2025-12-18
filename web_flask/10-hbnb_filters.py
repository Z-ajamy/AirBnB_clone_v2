#!/usr/bin/python3
"""
Starts a Flask web application.
Displays an HBNB filters page with dynamic content.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Fetches all State, City, and Amenity objects from storage,
    sorts them by name (A-Z), and renders the HBNB filters page.
    """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    
    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities, key=lambda amenity: amenity.name)
    
    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           amenities=sorted_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
