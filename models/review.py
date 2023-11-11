#!/usr/bin/python3

"""
This module where the class review that inherit from Base model.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    the class review for the
    feedbacks.
    """
    place_id = ""

    user_id = ""

    text = ""
