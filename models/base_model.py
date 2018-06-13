#!/usr/bin/python3
'''
Defines the class BaseModel
'''
import uuid
import models
from datetime import datetime


class BaseModel:
    '''Defines all common attributes/methods for other classes

    Attributes:
        id (string): unique user id
        created_at (datetime): time object was created
        updated__at (datetime): time object was  changed
    '''

    def __init__(self, *args, **kwargs):
        '''Initializes an object

        '''
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                else:
                    setattr(self, k, v)
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    time_format)
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    time_format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        '''Prints a string version of any object

        Return:
            returns the string version
        '''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''Updates updated_at with the current datetime

        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary of all keys/values of __dict__

        Return:
            returns a dictionary
        '''
        self_dict = self.__dict__.copy()
        self_dict['__class__'] = self.__class__.__name__
        self_dict['created_at'] = self.created_at.isoformat()
        self_dict['updated_at'] = self.updated_at.isoformat()
        return self_dict

    @classmethod
    def count(self):
        '''Returns a count of instance objects'''
        objects = models.storage.all()
        count = 0

        for obj in objects:
            if obj.__class__.__name__ == self.__class__.__name__:
                count += 1
        return count
