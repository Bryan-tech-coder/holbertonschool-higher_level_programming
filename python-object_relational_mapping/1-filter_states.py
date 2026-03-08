#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, database name.
Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
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

    cursor = db.cursor()
    # Select states starting with N, sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
