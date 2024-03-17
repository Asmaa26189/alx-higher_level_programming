#!/usr/bin/python3
"""
script
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    2-filter_states
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in c.fetchall()]
