#!/usr/bin/python3
"""a script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    argument = sys.argv[4]
    state = (session.query(State)
             .filter_by(name=argument).order_by(State.id).first())
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
