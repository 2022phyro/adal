#!/usr/bin/python3
"""This module is an introduction to SQLAlchemy.
It uses SQLAlchemy to save to a
certain database and simplfies the whole Query process
by using ORM instead of SQL"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)
