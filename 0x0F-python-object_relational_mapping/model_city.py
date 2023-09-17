#!/usr/bin/python3
"""Importing SQLAlchemy to let python connect to databases
and other necessary modules"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """Declaring a class named City that inherits from Base"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', backref='cities')
