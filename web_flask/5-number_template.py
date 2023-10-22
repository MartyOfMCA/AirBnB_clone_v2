#!/usr/bin/python3
"""
Define a method that handles requests to the
routes /, /hbnb and /c/<text> variable
and /python<text> using Flask.
"""
from flask import Flask, abort, render_template

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


@app.route("/number/<num>")
def number(num):
    """
    Handle requests to the route /number/some_number.

    Parameters
    num : integer
        The number sent to the route
    """
    if (num.isdigit()):
        return (f"{int(num)} is a number")

    abort(404)


@app.route("/number_template/<num>")
def number_template(num):
    if (num.isdigit()):
        return (render_template("5-number.html", num=num))

    abort(404)


if __name__ == "__main__":
    app.run(host="0")
