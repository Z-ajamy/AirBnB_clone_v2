#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INTEGER, FLOAT
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60),ForeignKey("cities.id") , nullable=False)
    user_id = Column(String(60),ForeignKey("users.id") , nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(FLOAT)
    longitude = Column(FLOAT)
    amenity_ids = []

    cities = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @properties
        def reviews(self):
            from models import storage
            from models.review import Review 
            review_list = []
            dic_of_all_reviews = storage.all(Review)
            for city in dic_of_all_reviews.values():
                if self.id == review.place_id:
                    review_list.append(city)
            return review_list
    else:
        reviews = relationship("Review", back_populates="place", cascade="all, delete, delete-orphan")

