#!/usr/bin/python3
"""
Define a module to serve requests for
states.
"""
from models.state import State
from models.state import City
from models import storage
from os import environ
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states")
def states():
    """ Retrieve a list of all states. """
    states = storage.all(State)

    return (render_template("9-states.html",
            states=states))


@app.route("/states/<id>")
def states_by_id(id):
    """ Retrieve a list of cities by states. """
    states = storage.all(State)
    my_dict = {}
    state = ""

    for key, value in states.items():
        if (value.id == id):
            my_dict[key] = value.cities
            state = value.name
            break

    return (render_template("9-states.html",
            states=my_dict, id=id, state=state))


@app.teardown_appcontext
def destroy(obj):
    storage.close()


if __name__ == "__main__":
    app.run(host="0")
