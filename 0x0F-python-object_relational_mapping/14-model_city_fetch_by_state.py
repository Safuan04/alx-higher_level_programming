#!/usr/bin/python3
"""Importing necessary modules"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    link = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(link)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City)\
        .join(City, State.id == City.state_id).all()
    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")
