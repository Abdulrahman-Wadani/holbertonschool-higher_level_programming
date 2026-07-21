#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur: MySQLdb.cursors.Cursor = conn.cursor()
    cur.execute(
        "{}".format("SELECT * FROM states WHERE name\
                    LIKE BINARY (%s) ORDER BY id ASC"),
        (sys.argv[4], ))
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
