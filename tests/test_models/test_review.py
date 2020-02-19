#!/usr/bin/python3
"""
    Contains the Review unittest.
"""
import os
import pep8
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class test_review(unittest.TestCase):
    """Tests review class"""

    @classmethod
    def setUpClass(cls):
        """Set up before every test method"""
        cls.review = Review()

    @classmethod
    def teardown(cls):
        """Remove test instances"""
        del cls.review
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_check(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/review.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstr_cls(self):
        """test dosctring class"""
        self.assertIsNotNone(Review.__doc__)

    def test_check_if_exits(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(hasattr(Review, "user_id"))

    def test_save(self):
        """Tests save method"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_id_func(self):
        """Test id functionality"""
        self.assertEqual(str, type(self.review.id))

    def test_created_func(self):
        """Test created_at functionality"""
        self.assertEqual(datetime, type(self.review.created_at))

    def test_updated_func(self):
        """Test updated_at functionality"""
        self.assertEqual(datetime, type(self.review.updated_at))

    def test_dict(self):
        """Tests to_dict method"""
        test_dict = self.review.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue("to_dict" in dir(self.review))


if __name__ == "__main__":
    unittest.main()
