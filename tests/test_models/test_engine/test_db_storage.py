#!/usr/bin/python3
"""Unit test for the file storage class
"""
import os
import sys
import MySQLdb
import unittest
import json
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'file')
class TestDBStorage(unittest.TestCase):
    """TestDBStorage resume
    Args:
        unittest (): Propertys for unit testing
    """
    def setUp(self):
        """ Set up test environment """
        dbUser = "hbnb_test"
        dbPassword = "hbnb_test_pwd"
        dbName = "hbnb_test_db"
        # Open database connection

    maxDiff = None

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        checker = pep8.StyleGuide(quiet=True)
        console_file = 'models/engine/db_storage.py'
        test_console_file = 'tests/test_models/test_engine/test_db_storage.py'
        result = checker.check_files([console_file, test_console_file])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_executable_file(self):
        """ Check if file have permissions to execute"""
        # Check for read access
        is_read_true = os.access('models/engine/db_storage.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/engine/db_storage.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/engine/db_storage.py', os.X_OK)
        self.assertTrue(is_exec_true)
