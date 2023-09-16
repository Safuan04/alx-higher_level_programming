#!/usr/bin/python3
"""Importng SQLAlchemy so that python can connect to a database"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Declaring a Class named State that inherits from Base"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
