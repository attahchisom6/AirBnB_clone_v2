#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="delete, delete-orphan, all")

    else if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns a list of city instances with state_id = state.id
            """
            c_list = []
            s_list = []

            obj_dict = models.storage.all()
            for key in obj_dict:
                classname = key.split(".")[0]
                if classname == "City":
                    s_list.append(obj_dict[key])
            for elem in s_list:
                if elem.state_id == self.id:
                    c_list.append(elem)
            return (c_list)
