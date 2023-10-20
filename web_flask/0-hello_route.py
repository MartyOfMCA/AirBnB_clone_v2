#!/usr/bin/python3
"""
Define a method that handles requests to the
route / using Flask.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
