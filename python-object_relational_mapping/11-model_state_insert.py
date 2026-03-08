#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Obtener argumentos
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Crear engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear nuevo estado
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Mostrar id del nuevo estado
    print(new_state.id)

    # Cerrar sesión
    session.close()
