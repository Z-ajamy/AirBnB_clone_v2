#!/usr/bin/python3
""" new class for sqlAlchemy """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all()


    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic_of_obj = {}
        if cls:
            list_of_obj = self.__session.query(cls).all()
        else:
            list_of_obj = []
            for z_cls in DBStorage.classes.values():
                list_of_obj.extend(self.__session.query(z_cls))
        for obj in list_of_obj:
            key = type(obj).__name__ + '.' + obj.id
            dic_of_obj[key] = obj

        return dic_of_obj
    
    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)


    def save(self):
        """save changes
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        Sec = sessionmaker(bind=self.__engine)
        Session = scoped_session(Sec)
        self.__session = Session()

