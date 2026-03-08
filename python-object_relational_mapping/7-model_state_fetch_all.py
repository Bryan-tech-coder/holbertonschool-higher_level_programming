#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Recibe usuario, contraseña y base de datos como argumentos
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Crear engine y conectar a MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener todos los objetos State ordenados por id
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Cerrar sesión
    session.close()
