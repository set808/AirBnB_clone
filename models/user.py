#!/usr/bin/python3
'''
Defines the User class
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Users for the AirBnB clone

    Attributes:
        email (str): the email of the User
        password (str): the password of the User
        first_name (str): the User's first name
        last_name (str): the User's last name
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
