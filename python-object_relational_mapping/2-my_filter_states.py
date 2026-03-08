#!/usr/bin/python3
"""
This script lists all states with a name matching the argument
from the database hbtn_0e_0_usa.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb

def main():
    """Connects to MySQL and prints all states matching the given name."""
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
    # Query with format as requested
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
