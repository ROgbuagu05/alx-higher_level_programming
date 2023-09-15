#!/usr/bin/python3
"""A Python file that contains the class definition of a City."""

from sqlalchemy import Integer, Column, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State")
