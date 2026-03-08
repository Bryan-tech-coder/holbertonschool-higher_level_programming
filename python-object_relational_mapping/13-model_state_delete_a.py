#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'"""
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

    # Buscar todos los estados que contengan 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Eliminar cada uno
    for state in states_to_delete:
        session.delete(state)

    # Aplicar cambios en la base de datos
    session.commit()

    # Cerrar sesión
    session.close()
