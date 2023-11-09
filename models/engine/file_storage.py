#!/usr/bin/python3
from base_model import BaseModel
import json
import os

class FileStorage:

	__file_path = "file.json"
    __objects = {}

	def all(self):
        return self.__objects
	def new(self, obj):
		key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
	def save(self):
		try:
            with open(self.__file_path, "r") as data_file:
                    data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        serialized_objects = {}
        for obj_key, obj_value in self.__objects.items():
                serialized_objects[obj_key] =obj_value.to_dict()
        data.update(serialized_objects)

        with open(self.__file_path, "w") as data_file:
            json.dump(data, data_file, indent=4)
	def reload(self):
		if self.__file_path is not None:
            try:
                with open(self.__file_path, "r") as data_file:
                    json_data = json.load(data_file)

                    for key, value in json_data.items():
                        class_name, obj_id = key.split('.')
                        class_obj = globals()[class_name]
                        
                        self.__objects[key] = class_obj(**value)
            except FileNotFoundError:
                pass