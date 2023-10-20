#!/usr/bin/python3
"""
Define a method that handles requests to the
routes /, /hbnb and /c/<text> variable using Flask.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    """ Handle requests to the root directory """
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """ Handle request to the hbnb route """
    return ("HBNB")


@app.route("/c/<text>")
def c_variable(text):
    """
    Handle requests to the route c.

    Parameters
    text : string
        The value sent to the route.
    """
    return (f"C {text.replace('_', ' ')}")


if __name__ == "__main__":
    app.run(host="0")
