#!/usr/bin/python3
"""
    Contains the State unittest.
"""
import os
import pep8
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class test_state(unittest.TestCase):
    """Tests state class"""

    @classmethod
    def setUpClass(cls):
        """Set up before every test method"""
        cls.state = State()

    @classmethod
    def teardown(cls):
        """Remove test instances"""
        del cls.state
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_check(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/state.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstr_cls(self):
        """Test docstring class"""
        self.assertIsNotNone(State.__doc__)

    def test_check_if_exits(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(State, "name"))

    def test_save(self):
        """Tests save method"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_id_func(self):
        """Test id functionality"""
        self.assertEqual(str, type(self.state.id))

    def test_created_func(self):
        """Test created_at functionality"""
        self.assertEqual(datetime, type(self.state.created_at))

    def test_updated_func(self):
        """Test updated_at functionality"""
        self.assertEqual(datetime, type(self.state.updated_at))

    def test_dict(self):
        """Tests to_dict method"""
        test_dict = self.state.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue("to_dict" in dir(self.state))


if __name__ == "__main__":
    unittest.main()
