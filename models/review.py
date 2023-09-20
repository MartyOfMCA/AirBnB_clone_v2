#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ A class to store reviews """

    __tablename__ = "reviews"

    if (environ.get("HBNB_TYPE_STORAGE", "file") == "db"):
        text = Column(String(1024), nullable=False)
        place_id = Column(ForeignKey("places.id"),
                          nullable=False)
        user_id = Column(ForeignKey("users.id"),
                         nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
