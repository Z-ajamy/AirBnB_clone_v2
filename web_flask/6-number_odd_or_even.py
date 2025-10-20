#!/usr/bin/python3
"""
Starts a Flask web application with more complex template rendering.
"""
from flask import Flask, render_template

app = Flask(__name__)
# By setting strict_slashes=False globally for the app instance,
# you don't need to repeat it in every route decorator.
# This is an optional but cleaner approach.
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Displays an HTML page only if n is an integer."""
    return render_template("5-number.html", n=n)


# CORRECTED: Function name is now unique.
@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """Displays an HTML page indicating if n is even or odd."""
    # CORRECTED: The logic for checking even/odd was reversed.
    # The condition must be explicit: n % 2 == 0.
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", number=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
