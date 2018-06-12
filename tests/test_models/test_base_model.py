#!/usr/bin/python3
'''
Defines unittets for BaseModel class
'''
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    '''Testing BaseModel Class

    '''

    @classmethod
    def setUpClass(cls):
        cls.bm1 = BaseModel()
        cls.bm1.name = "Holberton"
        cls.bm1.my_number = 89

    @classmethod
    def tearDownClass(cls):
        del cls.bm1

    def test_base_model_style(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    def test_base_model_docstrings(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_base_model_init(self):
        self.assertTrue(isinstance(self.bm1, BaseModel))
        self.assertEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_base_model_save(self):
        self.bm1.save()
        self.assertNotEqual(self.bm1.created_at, self.bm1.updated_at)

    def test_base_model_to_dict(self):
        bm1_dict = self.bm1.to_dict()
        self.assertIsInstance(bm1_dict['created_at'], str)
        self.assertIsInstance(bm1_dict['updated_at'], str)
        self.assertEqual(self.bm1.__class__.__name__, 'BaseModel')
