#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class for storing state entries """

    __tablename__ = "states"

    if (environ.get("HBNB_TYPE_STORAGE", "file") == "db"):
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete",
                              backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """ Obtains the cities for a state """
        from models import storage

        my_cities = []
        my_dict = storage.all(City)

        for key, value in my_dict.items():
            if (value.state.id == self.id):
                my_cities.append(value)

        return (my_cities)
