#!/usr/bin/python3
"""
Place Module for HBNB project
Defines the Place class and the place_amenity association table.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, INTEGER, FLOAT
from sqlalchemy.orm import relationship
from os import getenv

# --- Association Table for Many-to-Many relationship ---
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """
    A class to represent a place with various attributes and relationships.
    """
    __tablename__ = "places"

    # --- Columns Definition ---
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, nullable=False, default=0)
    number_bathrooms = Column(INTEGER, nullable=False, default=0)
    max_guest = Column(INTEGER, nullable=False, default=0)
    price_by_night = Column(INTEGER, nullable=False, default=0)
    latitude = Column(FLOAT, nullable=True)
    longitude = Column(FLOAT, nullable=True)

    # --- Attribute for FileStorage Only ---
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = []

    # --- Conditional Relationships (DBStorage) vs Getters (FileStorage) ---
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # --- Relationships for DBStorage ---
        
        # (Fix 1: Moved inside 'if' block)
        user = relationship("User", back_populates="places")
        
        # (Fix 1: Moved inside 'if' block | Fix 2: Renamed to 'city')
        city = relationship("City", back_populates="places")

        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete, delete-orphan")
        
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        # --- Getters/Setters for FileStorage ---

        @property
        def reviews(self):
            """
            Returns a list of Review instances for FileStorage.
            """
            from models import storage
            from models.review import Review
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            Returns a list of Amenity instances for FileStorage.
            """
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            Handles appending an Amenity's ID for FileStorage.
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
