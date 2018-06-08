#!/usr/bin/python3
'''
Defines the FileStorage class
'''
import json
from models.base_model import BaseModel

class FileStorage:
    '''Class that stores objects in JSON strings

    Attributes:
    file_path (str): path to the JSON file
    objects (dict): stores all objects by class
    '''

    __file_path = '../file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects

        Return:
            returns __objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Sets new object in __objects dictionary

        '''
        k = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        '''Serializes __objects to the JSON file

        '''
        save_dict = {}
        for k, v in FileStorage.__objects.items():
            v_dict = v.to_dict()
            save_dict[k] = v_dict
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(save_dict, f)

    def reload(self):
        '''Deserialize the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dicts = json.load(f)
                for k, v in dicts.items():
                    obj = eval(v['__class__'])(**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return
