#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Unittests for class Amenity"""

    def __init__(self, *args, **kwargs):
        """ Intialize test """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Tests name """
        new = self.value()
        new.name = "hello"
        self.assertEqual(type(new.name), str)
