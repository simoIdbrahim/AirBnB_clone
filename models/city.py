#!/usr/bin/python3
"""
This module where the class city that represent
the cities available in the website.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class city for all the cities in the site.
    Attributes:
    state_id(str): city unique id.
    name(str): City name.
    """
    state_id = ""

    name = ""
