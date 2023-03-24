#!/usr/bin/python3
"""class defining a database storage"""
from os import getenv
from models import syorage
from models.base_model import Base
from sqlalchemy import create_session
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.State import State
from models.user import User


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
        engine = self.__engine

        user = getenv("HBNB_MYSQL_USER")
        Pas = getenv("HBNB_MYSQL_PWD")
        host getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        server_url = "mysql+mysqldb://{}.{}@{}:3306/{}".format(uaer, pas, host, db)
        engine = create_engine(server_url, pool_pre_ping=True)
        session = sessionmaker()
        if env == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """querying to returnl all elments in  cls else, return all element
        Return: a dictoonary representation of the objects
        """
        session = self.__session()

        my_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
            return (my_dict)
        else:
            class_list = [User, Place, Amenity, Review, State, City]
            for classes in class_list:
                query = session.query(classes)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                my_dict[key] = elem
            return (my_dict)

    def new(self, obj):
        """adding a new object to the current database session
        """
        self._session.add(obj)

    def save(self):
        """commit all changes to the current database
        """
        self.__session.commit()

    def delete(self, obj):
        """delete from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """initilizing session yo create table"""
        engine = self.__engine
        session = self.__session()

        Base.metadata.create_all(egine)
        raw_session = sessionmaker(bind=engine, expire_on_commit=False)
        thread_free_session = scoped_session(raw_session)
        thread_free_session = session

    def close(self):
        """close the session"""
        self.__session.close()
