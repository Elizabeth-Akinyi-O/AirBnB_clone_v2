#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Test class Review """

    def __init__(self, *args, **kwargs):
        """ Initialize test """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test place_id """
        new = self.value()
        new.place_id = "2"
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test user_id """
        new = self.value()
        new.user_id = "testing"
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Test text """
        new = self.value()
        new.text = "hello"
        self.assertEqual(type(new.text), str)
