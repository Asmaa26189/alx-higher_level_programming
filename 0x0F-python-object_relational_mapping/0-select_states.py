#!/usr/bin/python3
"""
script
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    0-select_states
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
