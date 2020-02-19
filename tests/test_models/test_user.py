#!/usr/bin/python3
"""
    Contains the User unittest.
"""
import os
import pep8
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class test_user(unittest.TestCase):
    """Tests user class"""
    @classmethod
    def setUpClass(cls):
        """Set up before every test method"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "airbnb@holbertonshool.com"
        cls.user.password = "root"

    @classmethod
    def tearDownClass(cls):
        """Remove test instances"""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_check(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_sub_class(self):
        """Test is subclass"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_check_func(self):
        """Test checking for functions"""
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Checks if the methods exists"""
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("id" in self.user.__dict__)
        self.assertTrue("created_at" in self.user.__dict__)
        self.assertTrue("updated_at" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)

    def test_attr_str(self):
        """Checks if the attibutes are strings"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save(self):
        """Tests save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Tests to_dict method"""
        self.assertEqual("to_dict" in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
