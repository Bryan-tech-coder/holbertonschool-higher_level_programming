#!/usr/bin/python3
"""Changes the name of a State object in the database hbtn_0e_6_usa"""
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

    # Buscar el estado con id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Cambiar nombre si existe
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Cerrar sesión
    session.close()
