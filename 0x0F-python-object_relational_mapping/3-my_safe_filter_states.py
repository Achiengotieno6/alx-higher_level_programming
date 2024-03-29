#!/usr/bin/python3
"""Lists all states safely filtered by name from a database."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]
