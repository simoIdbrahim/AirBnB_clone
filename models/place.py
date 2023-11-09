#!/usr/bin/python3
"""
This module the class place that inherit from
basemodel and hold all the places available.
"""

from models.base_model import BaseModel

class Place(BaseModel):

	"""
	Class plase that hold the offers that will be shoween
	"""

	city_id = ""
	amenity_ids = []
	user_id = ""
	max_guest = 0
	price_by_night = 0
	name = ""
	description = ""
	number_bathrooms = 0
	latitude = 0.0
	longitude = 0.0
	number_rooms = 0
    
