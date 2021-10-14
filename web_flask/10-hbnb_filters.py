#!/usr/bin/python3
""" script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def removeSQLAlchemySession(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
