#!/usr/bin/python3
"""Module 5-script: starts a Flask web application
    listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable
        replace underscore _ symbols with a space"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def nIsNumber(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberOddEven(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        string = "{} is even".format(n)
    else:
        string = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', string=string)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
