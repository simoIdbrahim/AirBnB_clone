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
		pass
	save(self):
		pass
	reload(self):
		pass