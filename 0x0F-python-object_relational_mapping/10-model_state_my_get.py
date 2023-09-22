#!/usr/bin/python3
"""This prints a State object by name from a database."""
import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
