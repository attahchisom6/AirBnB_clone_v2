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
        self.obj = BaseModel

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
        default = self.obj()
        self.assertEqual(type(default), self.obj)

    def test_init(self):
        """testing the initialization ofhe default class"""
        self.assertIsInstance(self.obj(), BaseModel)
        if BaseModel is not self.obj:
            self.assertIsInstance(self.obj(), Base)
        else:
            self.assertNotIsInstance(self.obj(), Base)

    def test_kwargs(self):
        """testing the dictionary instances of the class"""
        k = self.obj()
        copy = k.to_dict()
        new_dict = BaseModel(**copy)
        self.assertFalse(new_dict is copy)

    def test_kwargs_int(self):
        """testing dictionary with int objects"""
        k = self.obj()
        copy = k.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_dict = BaseModel(**copy)


if __name__ == "__main__":
    unittest.main()
