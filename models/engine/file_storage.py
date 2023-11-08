#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage:

	__file_path = "file.json"
    __objects = {}

	def all(self):
        return self.__objects
	new(self, obj):
		key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
	save(self):
		pass
	reload(self):
		pass