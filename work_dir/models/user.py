#!/usr/bin/python3
"""defining elements of the class `User`
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a table for the class User"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship(
            'Place', backref='user', cascade="delete, delete-orphan, all")
    reviews = relationship(
            "Review", backref="user", cascade="delete, delete-orphan, all")
