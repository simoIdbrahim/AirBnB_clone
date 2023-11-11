#!/usr/bin/python3
"""
BaseModel Module

This module defines the BaseModel class, which serves as the parent class
for all other classes used in the AirBnB clone project.
It handles the initialization, serialization, and deserialization of instances.
"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """
    The BaseModel class defines common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel class. Initializes instance
        attributes based on provided
        keyword arguments or generates default values for id, created_at,
        and updated_at.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(self.created_at, time_format)
            self.updated_at = datetime.strptime(self.updated_at, time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance,
        including its class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes into a dictionary representation
        with 'simple object type'.
        """
        result_dict = {}
        result_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result_dict[key] = value.isoformat()
            else:
                result_dict[key] = value
        return result_dict
