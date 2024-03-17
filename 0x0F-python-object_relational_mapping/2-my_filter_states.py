#!/usr/bin/python3
"""
script
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    1-filter_states
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    text = "SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4])
    c.execute(text)
    [print(state) for state in c.fetchall()]
