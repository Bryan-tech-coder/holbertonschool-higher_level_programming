#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <username> <password> <database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    # Query all cities with their state names in a single execute()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
