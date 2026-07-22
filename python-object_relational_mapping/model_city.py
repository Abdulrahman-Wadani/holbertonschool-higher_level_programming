#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base =
declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Class City that inherits from Base and links to the MySQL table 'cities'
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
