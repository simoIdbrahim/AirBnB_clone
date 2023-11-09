#!/usr/bin/python3
"""
This module is where the user class thet inherit from
Basemodel and represent a client in the bnbproject.
"""

from models.base_model import BaseModel

class User(BaseModel):
	"""
    Class user that inherit from BaseModel
	and hold the data of a user.
    """
	email = ""

    password = ""

    first_name = ""

    last_name = ""