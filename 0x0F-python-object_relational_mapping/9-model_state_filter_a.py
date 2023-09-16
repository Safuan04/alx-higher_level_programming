#!/usr/bin/python3
"""Importing necessary modules"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    server = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(server)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like("%a%"))
    for state in result:
        print(f"{state.id}: {state.name}")
