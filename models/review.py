#!/usr/bin/python3
'''
Defines the Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Reviews for Hbnb application

    Attributes:
        place_id (str): the Place.id for Review
        user_id (str): the User.id giving the Review
        text (str): the text of the Review
    '''

    place_id = ''
    user_id = ''
    text = ''
