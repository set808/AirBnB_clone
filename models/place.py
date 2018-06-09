#!/usr/bin/python3
'''
Defines the Place class
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Places for Hbnb application

    Attributes:
        city_id (str): will be the City.id
        user_id (str): will be the User.id
        name (str): name of the Place
        description (str): description of the Place
        number_rooms (int): number of rooms in the Place
        number_bathrooms (int): number of bathrooms in the Place
        max_guest (int): maximum number of guests in the Place
        price_by_night (int): the nightly price of the Place
        latitude (float): the latitude of the Place
        longitude (float): the longitude of the Place
        amenity_ids (list): list of  Amenity.id of the Place
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
