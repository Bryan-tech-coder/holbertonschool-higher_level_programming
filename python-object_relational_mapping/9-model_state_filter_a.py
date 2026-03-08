#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa"""
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

    # Filtrar estados que contienen 'a' (mayúscula o minúscula según tu DB)
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Mostrar resultados
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Cerrar sesión
    session.close()
