#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
import models
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    #defining class attributes1
    id = Column(String(60), nullable=False, unique=True, primary_key=True)

    created_at = Column(DateTime, nullable=False,
            default=datetime.utcnow())

    updated_at = Column(DateTime, nullable=False,
            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """initializing instance attribute of our class

        Args:
            @args: argument vector
            @kwargs: dictionay parameters

        Attributes:
            @id:unique uuid
            @created_at: object created now
            @uodated_at: object updted now
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

                if key=="created_at" or key=="updated_at":
                    value = datetime.strptime(value,
                    "%Y-%m-%dT%H:%M:%S.%f")
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

            if "created_at" not in kwargs:
                self.created_at = datetime.now()

            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

            else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representation of an object"""
        return (self.__str__())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          str(type(self).__name__)})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """call the delete from Filestorage module
        """
        models.storage.delete(self)
