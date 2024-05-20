#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ
from os import getenv

STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


if environ.get('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
