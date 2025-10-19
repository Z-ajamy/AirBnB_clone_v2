#!/usr/bin/python3
"""a script that starts a Flask web application"""

from . import app

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

