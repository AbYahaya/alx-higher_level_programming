#!/usr/bin/python3
"""
Project was carried out by Ab Yahaya
3/16/2024
"""
import MySQLdb
import sys

if __name__ == '__main__':
    entered_args = sys.argv
    if len(entered_args) != 4:
        print("You have to enter username, passwd, database_nmae")
        exit(1)
    username = entered_args[1]
    password = entered_args[2]
    database = entered_args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
