#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        melissa = User()
        melissa.id = 999999
        melissa.name = "Melissa"
        m_storage.new(melissa)
        key = melissa.__class__.__name__ + "." + str(melissa.id)
        #print(instances_dic[key])
        self.assertIsNotNone(instances_dic[key])

    def test_reload_empty(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("""{"Place.5e817d8e-f407-4baa-8fcc-8326e6bca20e": {"id": "5e817d8e-f407-4baa-8fcc-8326e6bca20e", "created_at": "2018-06-12T21:51:53.933617", "updated_at": "2018-06-12T21:51:53.933617", "__class__": "Place"}, "State.0a921bcb-7b08-4167-b680-c414f9656844": {"id": "0a921bcb-7b08-4167-b680-c414f9656844", "created_at": "2018-06-12T21:51:56.316635", "updated_at": "2018-06-12T21:51:56.316635", "__class__": "State"}, "City.432003f2-dd04-4cfe-9cea-d4ffb2f32b98": {"id": "432003f2-dd04-4cfe-9cea-d4ffb2f32b98", "created_at": "2018-06-12T21:51:58.312707", "updated_at": "2018-06-12T21:51:58.312707", "__class__": "City"}, "Amenity.01675e9c-5355-423d-a4e8-7bca9f28f2a7": {"id": "01675e9c-5355-423d-a4e8-7bca9f28f2a7", "created_at": "2018-06-12T21:52:02.041651", "updated_at": "2018-06-12T21:52:02.041651", "__class__": "Amenity"}, "Review.e5d7eff1-aeda-4a5b-bb48-22abd6cd785d": {"id": "e5d7eff1-aeda-4a5b-bb48-22abd6cd785d", "created_at": "2018-06-12T21:52:04.868774", "updated_at": "2018-06-12T21:52:04.868774", "__class__": "Review"}, "User.596de9fc-c740-4359-8eda-187f8e12d668": {"id": "596de9fc-c740-4359-8eda-187f8e12d668", "created_at": "2018-06-12T21:56:44.156849", "updated_at": "2018-06-12T21:56:44.156849", "__class__": "User"}, "BaseModel.ec566da4-cf8c-4a6d-82e1-98809963f8e2": {"id": "ec566da4-cf8c-4a6d-82e1-98809963f8e2", "created_at": "2018-06-12T21:56:47.740809", "updated_at": "2018-06-12T21:56:47.740809", "__class__": "BaseModel"}}""")
        a_storage.reload()
        self.assertEqual(a_storage.all(), json.loads("""{"Place.5e817d8e-f407-4baa-8fcc-8326e6bca20e": {"id": "5e817d8e-f407-4baa-8fcc-8326e6bca20e", "created_at": "2018-06-12T21:51:53.933617", "updated_at": "2018-06-12T21:51:53.933617", "__class__": "Place"}, "State.0a921bcb-7b08-4167-b680-c414f9656844": {"id": "0a921bcb-7b08-4167-b680-c414f9656844", "created_at": "2018-06-12T21:51:56.316635", "updated_at": "2018-06-12T21:51:56.316635", "__class__": "State"}, "City.432003f2-dd04-4cfe-9cea-d4ffb2f32b98": {"id": "432003f2-dd04-4cfe-9cea-d4ffb2f32b98", "created_at": "2018-06-12T21:51:58.312707", "updated_at": "2018-06-12T21:51:58.312707", "__class__": "City"}, "Amenity.01675e9c-5355-423d-a4e8-7bca9f28f2a7": {"id": "01675e9c-5355-423d-a4e8-7bca9f28f2a7", "created_at": "2018-06-12T21:52:02.041651", "updated_at": "2018-06-12T21:52:02.041651", "__class__": "Amenity"}, "Review.e5d7eff1-aeda-4a5b-bb48-22abd6cd785d": {"id": "e5d7eff1-aeda-4a5b-bb48-22abd6cd785d", "created_at": "2018-06-12T21:52:04.868774", "updated_at": "2018-06-12T21:52:04.868774", "__class__": "Review"}, "User.596de9fc-c740-4359-8eda-187f8e12d668": {"id": "596de9fc-c740-4359-8eda-187f8e12d668", "created_at": "2018-06-12T21:56:44.156849", "updated_at": "2018-06-12T21:56:44.156849", "__class__": "User"}, "BaseModel.ec566da4-cf8c-4a6d-82e1-98809963f8e2": {"id": "ec566da4-cf8c-4a6d-82e1-98809963f8e2", "created_at": "2018-06-12T21:56:47.740809", "updated_at": "2018-06-12T21:56:47.740809", "__class__": "BaseModel"}}""")
