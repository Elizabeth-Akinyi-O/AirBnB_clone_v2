#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test class City """

    def __init__(self, *args, **kwargs):
        """ Initialize tests """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test state id """
        new = self.value()
        self.assertEqual(str(new.__class__.__name__), "City")

    def test_table_name(self):
        """ Test name """
        new = self.value()
        self.assertEqual(new.__tablename__, "cities")

    def test_state_id(self):
        """ Test state id """
        new = self.value()
        new.state_id = "1"
        self.assertEqual(new.state_id, "1")
