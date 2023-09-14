#!/usr/bin/python3
"""
Lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(
        State.name.ilike("%a%")).order_by(State.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
