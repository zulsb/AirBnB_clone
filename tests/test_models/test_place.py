#!/usr/bin/python3
"""
    Contains the Place unittest.
"""
import os
import pep8
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class test_place(unittest.TestCase):
    """Tests place class"""

    @classmethod
    def setUpClass(cls):
        """Set up before every test method"""
        cls.place = Place()

    @classmethod
    def teardown(cls):
        """Remove test instances"""
        del cls.place
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_style(self):
        """ Test pep8 style"""
        p = pep8.StyleGuide(quiet=True)
        res = p.check_files(["models/place.py"])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstr_cls(self):
        """Test docstring class"""
        self.assertIsNotNone(Place.__doc__)

    def test_check_if_exits(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_save(self):
        """Tests save method"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_id_func(self):
        """Test id"""
        self.assertEqual(str, type(self.place.id))

    def test_created_func(self):
        """Test created_at functionality"""
        self.assertEqual(datetime, type(self.place.created_at))

    def test_updated_func(self):
        """Test updated_at functionality"""
        self.assertEqual(datetime, type(self.place.updated_at))

    def test_dict(self):
        """Tests to_dict method"""
        test_dict = self.place.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue("to_dict" in dir(self.place))


if __name__ == "__main__":
    unittest.main()
