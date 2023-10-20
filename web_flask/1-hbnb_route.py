#!/usr/bin/python3
"""
Define a method that handles requests to the
routes / and /hbnb using Flask.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0")
