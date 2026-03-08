#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Obtener argumentos: usuario, contraseña, base de datos
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Crear engine y conectar a MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener el primer estado ordenado por id
    first_state = session.query(State).order_by(State.id).first()

    # Verificar si existe un registro
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Cerrar sesión
    session.close()
