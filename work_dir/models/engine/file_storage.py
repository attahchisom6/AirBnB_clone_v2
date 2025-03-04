#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """returns dictionary list of all object
        """
        my_dict = {}
        if cls:
            dictt = self.__objects
            for key in dictt.keys():
                classname = key[:key.find(".")]
                if classname == cls.__name__:
                    my_dict[key] = self.__objects[key]
            return (my_dict)
        else:
            return (self.__objects)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            className = type(obj).__name__
            classId = obj.id
            key = "{}.{}".format(className, classId)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                temp = json.load(f)
                for key, value in temp.items():
                        value = eval(value["__class__"])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an instance within(that is an already existant obj) the
        class
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
        return
