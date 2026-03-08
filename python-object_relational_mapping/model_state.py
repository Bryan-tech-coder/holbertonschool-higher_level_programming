#!/usr/bin/python3
"""Defines the State class and Base for SQLAlchemy ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Base class for all models

class State(Base):
    """State class mapped to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
