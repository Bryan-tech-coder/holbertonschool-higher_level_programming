#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import sys

try:
    import MySQLdb
except ModuleNotFoundError:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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
    # SQL injection safe query using placeholders
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    db.close()
