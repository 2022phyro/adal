#!/usr/bin/python3
"""This script uses sqlalchemy to list all
the states in a table"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(asc(State.id)).all()
    session.close()
    for state in states:
        print(f"{state.id}: {state.name}")
