#!/usr/bin/python3
"""
Define a method that handles requests to the
routes /, /hbnb and /c/<text> variable
and /python<text> using Flask.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    """ Handle requests to the root directory """
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """ Handle request to the route /hbnb """
    return ("HBNB")


@app.route("/c/<text>")
def c_variable(text):
    """
    Handle requests to the route /c.

    Parameters
    text : string
        The value sent to the route.
    """
    return (f"C {text.replace('_', ' ')}")


@app.route("/python/<text>")
def python_variable(text):
    """
    Handle requests to the route /python/something.

    Parameters
    text : string
        The value sent to the route.
    """
    return (f"Python {text.replace('_', ' ')}")


@app.route("/python/")
def python():
    """
    Handle requests to the route /python. This
    function handles requests to the python
    route directly.
    """
    return (f"Python is cool")


if __name__ == "__main__":
    app.run(host="0")
