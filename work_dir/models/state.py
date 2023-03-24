#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from mysqlalchemy import String, Column
from sqlalchemy.orm import relationship
from model import storage


class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade=(delete, all))

    @properties
    def cities(self):
        """returns a list of city instances with state_id = stTmate.id
        """
        c_list = []
        s_list = []

        obj_dict = storage.all()
        for key obj_dict:
            classname = key.split(".")[0]
            if classname == "City":
                s_list.append(key)
        for elem in s_list:
            if elem.state_id = State.id:
                c_list.append(elem)
        return (c_list)
