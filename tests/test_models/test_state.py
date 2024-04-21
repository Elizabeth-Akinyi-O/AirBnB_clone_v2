#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test class State """

    def __init__(self, *args, **kwargs):
        """ Initialize test """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_tablename(self):
        """ Test tablename """
        new = self.value()
        self.assertEqual((new.__tablename__), "states")

    def test_name(self):
        """ Test name """
        new = self.value()
        new.name = "California"
        self.assertEqual(new.name, "California")
