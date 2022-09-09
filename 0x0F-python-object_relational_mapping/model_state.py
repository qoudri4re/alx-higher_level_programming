#!/usr/bin/python3
"""A module containing the state model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
"""represents the base class for all tables"""


class State(Base):
    """represents a row in a states table"""

    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(lenght=128),
        nullable=False
    )
