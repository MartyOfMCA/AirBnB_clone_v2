#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Stores the amenities for a place """

    __tablename__ = "amenities"

    if (environ.get("HBNB_TYPE_STORAGE", "file") == "db"):
        name = Column(String(128), nullable=False)
    else:
        name = ""
