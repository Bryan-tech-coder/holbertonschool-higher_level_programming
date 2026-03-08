#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <user> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Crear engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtener todas las ciudades y su estado, ordenadas por city.id
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        # Acceder al nombre del estado mediante la relación FK
        state = session.query(State).filter(State.id == city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
