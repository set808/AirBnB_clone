#!/usr/bin/python3
'''
Defines the City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Cities for Hbnb application

    Attributes:
    state_id (str): will be State.id
        name (str): name of the States
    '''

    state_id = ''
    name = ''
