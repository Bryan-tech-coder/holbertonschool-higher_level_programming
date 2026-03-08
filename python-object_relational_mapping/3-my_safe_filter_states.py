#!/usr/bin/python3
"""
This script lists all states with a name matching the argument
from the database hbtn_0e_0_usa in a safe way (prevents SQL injection).
Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
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
    # Safe query using placeholders
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
