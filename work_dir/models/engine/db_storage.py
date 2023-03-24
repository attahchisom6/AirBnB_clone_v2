#!/usr/bin/python3
"""class defining a database storage"""
from os import getenv
from models.base_model import Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City


class DBStorage:
    """this engine will detine a databaese storage to our use
    """
    """private class attributes"""
    __engine = None
    __session = None

    """public instance method"""
    def __init__(self):
        """creating and connecting to server engine
        """
        user = getenv("HBNB_MYSQL_USER")
        pas = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        server_url = "mysql+mysqldb://{}:{}@{}/{}".format(user, pas, host, db)
        self.__engine = create_engine(server_url, pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """querying to returnl all elments in  cls else, return all element
        Return: a dictoonary representation of the objects
        """
        my_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
            return (my_dict)
        else:
            class_list = [User, Place, Amenity, Review, State, City]
            for classes in class_list:
                query = self.__session.query(classes)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
            return (my_dict)

    def new(self, obj):
        """adding a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes to the current database
        """
        self.__session.commit()

    def delete(self, obj):
        """delete from the current database session
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """initilizing session yo create table"""
        Base.metadata.create_all(self.__engine)
        raw_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(raw_session)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
