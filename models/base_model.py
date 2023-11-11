#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
import datetime
import models


class BaseModel:
    """the base model class."""

    def __init__(self, *args, **kwargs):
        """BaseModel constructor

        Args:
            *args: Unused.
            **kwargs (dict): Key/value.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

        time_format = '%Y-%m-%dT%H:%M:%S.%f'

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(
                        val, time_format)
                else:
                    self.__dict__[key] = val
        models.storage.new(self)

    def __str__(self):
        """ return the name of class and the id and the __dict__ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute and the current datetime """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance
        """

        this_dict = self.__dict__
        this_result = {}
        this_dict["__class__"] = self.__class__.__name__

        for key, val in this_dict.items():
            if isinstance(val, datetime.datetime):
                this_result[key] = val.isoformat()
            else:
                this_result[key] = val

        return this_result
