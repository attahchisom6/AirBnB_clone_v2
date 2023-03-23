#!/usr/bin/python3
"""Tgid module will test the base model
class
"""
from models.base_model import BaseModel, Base
from uuid import UUID
import unittest
import pycodestyle
import os

class test_baseModels(unittest.TestCase):
    """testing ouf class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def pycodestyle(self):
        """a method to test pep8 format"""
        style = pycodestyle.StyleGuilde(queit=True)
        result = style.file_checks(['models/base_models.py'])
        strr = "Found code styles errors (and warnings)."
        self.assertEqual(result.total_errors, 0, strr)

    def setUp(self):
        """configure the objects under test"""
        pass

    def tearDown(self):
        """frees the objects"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """testing the default case"""
        default = self.value()
        self.assertEqual(type(default), self.value)

    def test_init(self):
        """testing the initialization ofhe default class"""
        self.assertIsInstance(self.value(), BaseModel)
        if BaseModel is not self.value:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_kwargs(self):
        """testing the dictionary instances of the class"""
        k = self.value()
        copy = k.to_dict()
        new_dict = BaseModel(**copy)
        self.assertFalse(new_dict is copy)

    def test_kwargs_int(self):
        """testing dictionary with int objects"""
        k = self.value()
        copy = k.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_dict = BaseModel(**copy)


if __name__ == "__main__":
    unittest.main()
