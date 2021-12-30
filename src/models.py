import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False) 
    email = Column(String(250), nullable=False) 
    password = Column(String(250), nullable=False) 

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    home_planet = Column(Integer, nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation = Column(Integer, nullable=False)
    translation = Column(Integer, nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    weight = Column(Integer, nullable=False) 

class UserFavCharacters(Base):
    __tablename__ = 'userfavcharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character = relationship(Character)

    def to_dict(self):
        return {}

class UserFavPlanets(Base):
    __tablename__ = 'userfavplanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet = relationship(Planet)

    def to_dict(self):
        return {}

class UserFavVehicles(Base):
    __tablename__ = 'userfavvehicles'
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey('vehicle.id'))
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')