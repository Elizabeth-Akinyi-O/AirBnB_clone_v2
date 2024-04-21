#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Test class Place """

    def __init__(self, *args, **kwargs):
        """ Initialize test """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test city_id """
        new = self.value()
        self.assertEqual((new.city_id), None)

    def test_user_id(self):
        """ Test user_id """
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_name(self):
        """ Test name """
        new = self.value()
        self.assertEqual((new.name), None)

    def test_description(self):
        """ Test description """
        new = self.value()
        self.assertEqual((new.description), None)

    def test_number_rooms(self):
        """ Test number of rooms """
        new = self.value()
        self.assertEqual((new.number_rooms), None)

    def test_number_bathrooms(self):
        """ Test number of bathrooms """
        new = self.value()
        self.assertEqual((new.number_bathrooms), None)

    def test_max_guest(self):
        """ Test guest maximum # """
        new = self.value()
        self.assertEqual((new.max_guest), None)

    def test_price_by_night(self):
        """ Test price by night """
        new = self.value()
        self.assertEqual((new.price_by_night), None)

    def test_latitude(self):
        """ Test latitude """
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_longitude(self):
        """  Test longitude"""
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_amenity_ids(self):
        """ Test amenity ids """
        new = self.value()
        self.assertEqual((new.amenity_ids), [])
