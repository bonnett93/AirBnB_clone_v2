#!/usr/bin/python3
"""Module 1-hbnb_route: starts a Flask web application
    listening on 0.0.0.0, port 5000 with three routes"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """display “C ” followed by the value of the text variable
        replace underscore _ symbols with a space"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
