#!/usr/bin/python3
import MySQLdb
import MySQLdb.cursors
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        exit(1)
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur: MySQLdb.cursors.Cursor = conn.cursor()
    cur.execute("SELECT * FROM states  ORDER BY id")
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    conn.close()
