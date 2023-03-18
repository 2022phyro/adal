#!/usr/bin/python3
"""This script lists all State objects that contain the letter
a from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name.contains("a")
    ).order_by(asc(State.id))
    session.close()
    if not states:
        print("Nothing")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")
