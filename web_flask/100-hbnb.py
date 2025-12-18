#!/usr/bin/python3
"""
Starts a Flask web application.
Displays the main HBNB page with dynamic content.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_full_page():
    """
    Fetches all State, Amenity, and Place objects from storage,
    sorts them by name (A-Z), and renders the main HBNB page.
    """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    
    all_amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(all_amenities, key=lambda amenity: amenity.name)
    
    all_places = storage.all(Place).values()
    sorted_places = sorted(all_places, key=lambda place: place.name)
    
    return render_template('100-hbnb.html',
                           states=sorted_states,
                           amenities=sorted_amenities,
                           places=sorted_places)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)
