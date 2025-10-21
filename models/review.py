#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60),ForeignKey("places.id") , nullable=False)
    user_id = Column(String(60),ForeignKey("users.id") , nullable=False)
    text = Column(String(1024), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
