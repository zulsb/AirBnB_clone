#!/usr/bin/python3
"""
    Contains the Amenity unittest.
"""
import os
import pep8
import unittest
from datetime import datetime
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """Tests amenity class"""
    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.amenity = Amenity()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.amenity
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8style(self):
        """Pep8 style test"""
        p = pep8.StyleGuide(quiet=True)
        res = p.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_save(self):
        """Tests save method"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_check_if_exist(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(Amenity, "name"))

    def test_id(self):
        """Test id"""
        self.assertEqual(str, type(self.amenity.id))

    def test_created(self):
        """Test created"""
        self.assertEqual(datetime, type(self.amenity.created_at))

if __name__ == "__main__":
    unittest.main()
