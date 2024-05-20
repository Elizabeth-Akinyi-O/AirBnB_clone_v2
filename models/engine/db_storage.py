#!/usr/bin/python3
""" State module for the HBNB project """

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base


class DBStorage():
    """ SQL storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ Inits the sql db storage """

        dbUser = os.environ.get('HBNB_MYSQL_USER')
        dbPassword = os.environ.get('HBNB_MYSQL_PWD')
        dbHost = os.environ.get('HBNB_MYSQL_HOST')
        dbName = os.environ.get('HBNB_MYSQL_DB')
        mode = os.environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(dbUser, dbPassword,
                                             dbHost, dbName),
                                      pool_pre_ping=True)
        if (mode == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary with all the methods """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from console import HBNBCommand

        result = {}
        all_classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            for cls in all_classes:
                for row in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, row.id)
                    result[key] = row
        else:
            for row in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, row.id)
                result[key] = row

        return (result)

    def new(self, obj):
        """ Creates a new object """
        self.__session.add(obj)

    def save(self):
        """ Saves session in database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an obj from db """
        if not obj:
            return
        self.__session.delete(obj)

    def reload(self):
        """ Loads all tables in the database """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

    def close(self):
        """ Resets the session from the database """
        self.__session.close()
