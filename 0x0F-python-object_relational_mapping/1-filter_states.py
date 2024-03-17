#!/usr/bin/python3
"""
Project carried out by Ab Yahaya
3/17/2024
"""
import MySQLdb
import sys


if __name__ == '_main__':
    arguments = sys.argv
    if len(arguments) != 4:
        print("You have to enter username, password, database")
        exit(1)
    username = arguments[1]
    password = arguments[2]
    database = arguments[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                'N%' ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
