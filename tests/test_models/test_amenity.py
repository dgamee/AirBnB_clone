#!/usr/bin/python3

"""Testcase for Amentity"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        hold = Amenity()
        self.assertIn("id", hold.to_dict())
        self.assertIn("created_at", hold.to_dict())
        self.assertIn("updated_at", hold.to_dict())
        self.assertIn("__class__", hold.to_dict())

    def test_to_dict_contains_added_attributes(self):
        hold = Amenity()
        hold.middle_name = "Holbert"
        hold.my_number = 9
        self.assertEqual("Holbert", hold.middle_name)
        self.assertIn("my_number", hold.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        hold = Amenity()
        am_dict = hold.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        hold = Amenity()
        hold.id = "123456"
        hold.created_at = hold.updated_at = dt
        tdict = {
            "id": "123456",
            "__class__": "Amenity",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
        }
        self.assertDictEqual(hold.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        hold = Amenity()
        self.assertNotEqual(hold.to_dict(), hold.__dict__)

    def test_to_dict_with_arg(self):
        hold = Amenity()
        with self.assertRaises(TypeError):
            hold.to_dict(None)


if __name__ == "__main__":
    unittest.main()
