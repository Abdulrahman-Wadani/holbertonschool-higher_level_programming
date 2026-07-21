#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa.
Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
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

    # 3. تنفيذ استعلام الـ JOIN بطريقة الدمج النظيف بدون مسافات زائدة
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM states "
        "JOIN cities ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    conn.close()
