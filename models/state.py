#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import environ
from os import getenv

# Attempts to retrieve an environment variable named HBNB_TYPE_STORAGE.
# If this environment variable is not set, getenv will return None.
STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class - contains state ID and name """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if (environ.get("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """ Getter method for cities """
            from models import storage
            from models.city import City
            cities_dict = []
            for key in storage.all(City):
                if self.id in storage.all(City)[key].state_id:
                    cities_dict.append(storage.all(City)[key])
            return (cities_dict)
