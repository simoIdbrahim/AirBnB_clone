#!/usr/bin/python3
"""
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
import os
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    Class holds the serialization and deserialization
    of objects and the manipulation of data from json files.
    """


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns all stored objects as a dictionnary.
        """


        return self.__objects

    def new(self, obj):
        """
        add a new object
        """

        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        self.__objects[key] = obj


    def save(self):
        """
        Serializes dump data to file json).
        """

        data = {}

        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """
        Deserializes load data from filr json.
        """

        if os.path.exists(self.__file_path):

            try:
                with open(self.__file_path, "r",encoding="utf-8") as file_data:

                    data_jsonfile = json.load(file_data)
                    for key, value in data_jsonfile.items():
                        
                        if '.' in key:
                            class_name, obj_id = key.split('.')
                            class_obj = globals()[class_name]
                            new_instance = class_obj(**value)
                            self.new(new_instance)
                            self.__objects[key] = new_instance

            except FileNotFoundError:
                pass